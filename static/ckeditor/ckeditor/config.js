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
		},
		pre: true,
	};

	config.fontSize_defaultLabel = 'サイズ';
	config.font_defaultLabel = 'serif';

	config.toolbarGroups = [
		{name: 'pbckcode'},
		// your other buttons here
		// get information about available buttons here: bhttp://docs.ckeditor.com/?mobile=/guide/dev_toolbar
	];
	
	// CKEDITOR PLUGINS LOADING
	config.extraPlugins = 'pbckcode';

	//config.allowedContent = 'pre[*]{*}(*)'; 

	config.pbckcode = {
		// An optional class to your pre tag.
		cls: '',
	
		// The syntax highlighter you will use in the output view
		highlighter: 'PRETTIFY',
	
		// An array of the available modes for you plugin.
		// The key corresponds to the string shown in the select tag.
		// The value correspond to the loaded file for ACE Editor.
		modes: [
			['Python', 'python'],
			['HTML', 'html'], 
			['CSS', 'css'], 
			['PHP', 'php'], 
			['JS', 'javascript'],
		],
	
		// The theme of the ACE Editor of the plugin.
		theme: 'tomorrow_night',
	
		// Tab indentation (in spaces)
		tab_size: '4'
	};
};

CKEDITOR.addCss(".cke_editable{cursor:text; font-size: 16px; font-family: Arial, sans-serif;}");

//CKEDITOR.config.extraPlugins = "toc";
//CKEDITOR.config.format_tags = 'div';
