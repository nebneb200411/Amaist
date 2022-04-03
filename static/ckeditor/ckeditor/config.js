/**
 * @license Copyright (c) 2003-2021, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function (config) {
	config.language = 'ja';
	config.mathJaxLib = '//cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-AMS_HTML';
	config.allowedContent = {
		script: true,
		div: true,
		$1: {
			// This will set the default set of elements
			elements: CKEDITOR.dtd,
			attributes: true,
			styles: true,
			classes: true
		}
	};

};
