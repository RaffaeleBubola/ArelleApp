'''
Created on May 19, 2013

@author: Mark V Systems Limited
(c) Copyright 2013 Mark V Systems Limited, All rights reserved.
'''
from XbrlSemanticDB import XbrlSemanticDatabaseConnection
from XbrlStandardRoles import parentChild, summationItem
import os

def viewRelationships(request):
    dbConn = XbrlSemanticDatabaseConnection(request)
    _arcrole = dbConn.arcrole
    # tree roots before tree descendants of roots
    results = dbConn.execute("View Report", """
        {2} -- relationship set for labels
        -- get roots
        SELECT rs.relationship_set_id, rt.definition, rel.relationship_id, rel.tree_sequence, 
               0 AS tree_depth, rel.calculation_weight, a.aspect_id, lbl.value, a.balance, dt.name
        FROM report r, role_type rt, relationship_set rs, relationship rel, aspect a, data_type dt,
             label_relationship_set lrs, relationship lrel, resource lbl
        WHERE r.filing_id = {0}
        AND rt.document_id = r.report_schema_doc_id
        AND rs.document_id = r.report_schema_doc_id
        AND rs.link_role = rt.role_uri
        AND rs.arc_role = '{1}'
        AND rel.relationship_set_id = rs.relationship_set_id 
        AND a.aspect_id = rel.from_id AND rel.tree_sequence = 1
        AND dt.data_type_id = a.datatype_id
        AND lrel.relationship_set_id = lrs.relationship_set_id AND lrel.from_id = a.aspect_id
        AND lrel.to_id = lbl.resource_id AND lbl.role = 'http://www.xbrl.org/2003/role/label'
        UNION -- get descendants of root
        SELECT rs.relationship_set_id, rt.definition, rel.relationship_id, rel.tree_sequence, 
               rel.tree_depth, rel.calculation_weight, a.aspect_id, lbl.value, a.balance, dt.name
        FROM report r, role_type rt, relationship_set rs, relationship rel, aspect a, data_type dt,
             label_relationship_set lrs, relationship lrel, resource lbl
        WHERE r.filing_id = {0}
        AND rt.document_id = r.report_schema_doc_id
        AND rs.document_id = r.report_schema_doc_id
        AND rs.link_role = rt.role_uri
        AND rs.arc_role = '{1}'
        AND rel.relationship_set_id = rs.relationship_set_id 
        AND a.aspect_id = rel.to_id
        AND dt.data_type_id = a.datatype_id
        AND lrel.relationship_set_id = lrs.relationship_set_id AND lrel.from_id = a.aspect_id
        AND lrel.to_id = lbl.resource_id AND lbl.role = 'http://www.xbrl.org/2003/role/label'
        -- order by link role definition, sequence, and depth
        ORDER BY definition, tree_sequence, tree_depth
        """.format(dbConn.filingId, dbConn.arcrole, dbConn.withAspectLabelRelSetId))
    dbConn.close()
    docTree = {"rows": []}
    parentSubtree = {}
    prevRelSetId = None
    # results are in dependeny order due to recursive descent in doc_graph
    for result in results:
        relSetId, definition, relId, _seq, depth, weight, aspectId, name, balance, dataType = result
        if relSetId != prevRelSetId:
            prevRelSetId = relSetId
            parentSubtree.clear()
            # add link role
            rsRow = {"id": str(relSetId), "data": [definition], "rows": []}
            parentSubtree[-1] = rsRow # link role row
            docTree["rows"].append(rsRow)
        _parentDepth = depth - 1
        if _parentDepth in parentSubtree:
            _parentRow = parentSubtree[_parentDepth]
            if "rows" not in _parentRow:
                _parentRow["rows"] = []
            _rows = _parentRow["rows"]
            _data = [name]
            if _arcrole == parentChild:
                _data.append(dataType)
            elif _arcrole == summationItem:
                _data.append(weight)
                _data.append(balance)
            _row = {"id": "{}_{}".format(relSetId, aspectId if depth == 0 else relId),
                    "data": _data}
            _rows.append(_row)
            parentSubtree[depth] = _row
    return docTree

def selectRelationships(request):
    dbConn = XbrlSemanticDatabaseConnection(request)
    results = dbConn.execute("Select Aspects", """
        WITH selected_aspect(aspect_id) as (
           SELECT
           CASE WHEN (SELECT TRUE FROM aspect WHERE aspect_id = {2})
           THEN
              {2}::bigint
           ELSE (
              CASE WHEN (SELECT TRUE from relationship where relationship_id = {2})
              THEN (SELECT r.to_id FROM relationship r WHERE relationship_id = {2})
              ELSE (
                 CASE WHEN (SELECT TRUE from data_point where datapoint_id = {2})
                 THEN (SELECT d.aspect_id from data_point d where datapoint_id = {2})
                 ELSE 0::bigint
                 END
              ) END
           ) END
        )
        SELECT rs.relationship_set_id || '_' || rel.relationship_id
        FROM report r, relationship_set rs, relationship rel, selected_aspect sa
        WHERE r.filing_id = {0}
        AND rs.document_id = r.report_schema_doc_id
        AND rs.arc_role = '{1}'
        AND rel.relationship_set_id = rs.relationship_set_id 
        AND rel.to_id = sa.aspect_id
        LIMIT 1 -- only return first
        """.format(dbConn.filingId, dbConn.arcrole, dbConn.id))
    dbConn.close()
    return results
