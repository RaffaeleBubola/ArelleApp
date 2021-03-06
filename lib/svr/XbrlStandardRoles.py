

stdRoleKeys = dict(
    (k,v)
    for i, r in enumerate(
         "http://www.xbrl.org/2003/role/label",
         "http://www.xbrl.org/2003/role/terseLabel",
         "http://www.xbrl.org/2003/role/verboseLabel",
         "http://www.xbrl.org/2003/role/positiveLabel",
         "http://www.xbrl.org/2003/role/positiveTerseLabel",
         "http://www.xbrl.org/2003/role/positiveVerboseLabel",
         "http://www.xbrl.org/2003/role/negativeLabel",
         "http://www.xbrl.org/2003/role/negativeTerseLabel",
         "http://www.xbrl.org/2003/role/negativeVerboseLabel",
         "http://www.xbrl.org/2003/role/zeroLabel",
         "http://www.xbrl.org/2003/role/zeroTerseLabel",
         "http://www.xbrl.org/2003/role/zeroVerboseLabel",
         "http://www.xbrl.org/2003/role/totalLabel",
         "http://www.xbrl.org/2003/role/periodStartLabel",
         "http://www.xbrl.org/2003/role/periodEndLabel",
         "http://www.xbrl.org/2003/role/documentation",
         "http://www.xbrl.org/2003/role/definitionGuidance",
         "http://www.xbrl.org/2003/role/disclosureGuidance",
         "http://www.xbrl.org/2003/role/presentationGuidance",
         "http://www.xbrl.org/2003/role/measurementGuidance",
         "http://www.xbrl.org/2003/role/commentaryGuidance",
         "http://www.xbrl.org/2003/role/exampleGuidance",
         "http://www.xbrl.org/2003/role/reference",
         "http://www.xbrl.org/2003/role/definitionRef",
         "http://www.xbrl.org/2003/role/disclosureRef",
         "http://www.xbrl.org/2003/role/mandatoryDisclosureRef",
         "http://www.xbrl.org/2003/role/recommendedDisclosureRef",
         "http://www.xbrl.org/2003/role/unspecifiedDisclosureRef",
         "http://www.xbrl.org/2003/role/presentationRef",
         "http://www.xbrl.org/2003/role/measurementRef",
         "http://www.xbrl.org/2003/role/commentaryRef",
         "http://www.xbrl.org/2003/role/exampleRef",
         "http://www.xbrl.org/2003/role/calculationLinkbaseRef",
         "http://www.xbrl.org/2003/role/definitionLinkbaseRef",
         "http://www.xbrl.org/2003/role/labelLinkbaseRef",
         "http://www.xbrl.org/2003/role/presentationLinkbaseRef",
         "http://www.xbrl.org/2003/role/referenceLinkbaseRef",
         "http://www.xbrl.org/2003/role/link",
         "http://www.xbrl.org/2003/role/footnote",
         "http://www.xbrl.org/2003/arcrole/concept-label",
         "http://www.xbrl.org/2003/arcrole/concept-reference",
         "http://www.xbrl.org/2003/arcrole/fact-footnote",
         "http://www.xbrl.org/2003/arcrole/parent-child",
         "http://www.xbrl.org/2003/arcrole/summation-item",
         "http://www.xbrl.org/2003/arcrole/general-special",
         "http://www.xbrl.org/2003/arcrole/essence-alias",
         "http://www.xbrl.org/2003/arcrole/similar-tuples",
         "http://www.xbrl.org/2003/arcrole/requires-element")
    for n in ("_r{0}".format(i))
    for k, v in ((n,r),(r,n)))
