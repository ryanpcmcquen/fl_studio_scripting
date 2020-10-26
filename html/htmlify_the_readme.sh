#!/bin/sh
showdown makehtml -i README.md -o html/README.html \
    --openLinksInNewWindow --completeHTMLDocument \
    --omitExtraWLInCodeBlocks --parseImgDimensions --simplifiedAutoLink --literalMidWordUnderscores --strikethrough --tables --ghCodeBlocks --tasklists --smoothLivePreview --ghCompatibleHeaderId --encodeEmails
echo "<style>" >> html/README.html
cat html/foundation_and_showdown.css >> html/README.html
echo "</style>" >> html/README.html
