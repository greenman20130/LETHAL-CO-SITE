/**
 * @license Copyright (c) 2003-2023, CKSource Holding sp. z o.o. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */


CKEDITOR.on('instanceReady', function (ev) {
    ev.editor.dataProcessor.htmlFilter.addRules({
        elements: {
            $: function (element) {
                if (element.name == 'img') {
                    var style = element.attributes.style || '';
                    if (!style.match(/max-width/)) {
                        style += ';max-width: 800px';
                    }
                    if (!style.match(/max-height/)) {
                        style += ';max-height: 700px';
                    }
                    element.attributes.style = style;
                }
            }
        }
    });
});