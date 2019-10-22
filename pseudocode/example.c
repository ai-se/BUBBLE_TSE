/* libxml2-2.9.9/parser.c:8347 */
const xmlChar * 
xmlParseAttribute(xmlParserCtxtPtr ctxt, xmlChar **value) {
    const xmlChar *name;
    ...
    // obtain attribute name from input
    name = xmlParseName(ctxt);
    // check if attribute equals to a specification.
    if (xmlStrEqual(name, "xml:space")){
        ...
    }
}
