<!DOCTYPE html>
<!-- saved from url=(0096)https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CWC23QUALIF -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style id="ace-one-dark">.ace-one-dark .ace_gutter {
    background: #282c34;
    color: #6a6f7a
}

.ace-one-dark .ace_print-margin {
    width: 1px;
    background: #e8e8e8
}

.ace-one-dark {
    background-color: #282c34;
    color: #abb2bf
}

.ace-one-dark .ace_cursor {
    color: #528bff
}

.ace-one-dark .ace_marker-layer .ace_selection {
    background: #3d4350
}

.ace-one-dark.ace_multiselect .ace_selection.ace_start {
    box-shadow: 0 0 3px 0 #282c34;
    border-radius: 2px
}

.ace-one-dark .ace_marker-layer .ace_step {
    background: #c6dbae
}

.ace-one-dark .ace_marker-layer .ace_bracket {
    margin: -1px 0 0 -1px;
    border: 1px solid #747369
}

.ace-one-dark .ace_marker-layer .ace_active-line {
    background: rgba(76, 87, 103, .19)
}

.ace-one-dark .ace_gutter-active-line {
    background-color: rgba(76, 87, 103, .19)
}

.ace-one-dark .ace_marker-layer .ace_selected-word {
    border: 1px solid #3d4350
}

.ace-one-dark .ace_fold {
    background-color: #61afef;
    border-color: #abb2bf
}

.ace-one-dark .ace_keyword {
    color: #c678dd
}

.ace-one-dark .ace_keyword.ace_operator {
    color: #c678dd
}

.ace-one-dark .ace_keyword.ace_other.ace_unit {
    color: #d19a66
}

.ace-one-dark .ace_constant.ace_language {
    color: #d19a66
}

.ace-one-dark .ace_constant.ace_numeric {
    color: #d19a66
}

.ace-one-dark .ace_constant.ace_character {
    color: #56b6c2
}

.ace-one-dark .ace_constant.ace_other {
    color: #56b6c2
}

.ace-one-dark .ace_support.ace_function {
    color: #61afef
}

.ace-one-dark .ace_support.ace_constant {
    color: #d19a66
}

.ace-one-dark .ace_support.ace_class {
    color: #e5c07b
}

.ace-one-dark .ace_support.ace_type {
    color: #e5c07b
}

.ace-one-dark .ace_storage {
    color: #c678dd
}

.ace-one-dark .ace_storage.ace_type {
    color: #c678dd
}

.ace-one-dark .ace_invalid {
    color: #fff;
    background-color: #f2777a
}

.ace-one-dark .ace_invalid.ace_deprecated {
    color: #272b33;
    background-color: #d27b53
}

.ace-one-dark .ace_string {
    color: #98c379
}

.ace-one-dark .ace_string.ace_regexp {
    color: #e06c75
}

.ace-one-dark .ace_comment {
    font-style: italic;
    color: #5c6370
}

.ace-one-dark .ace_variable {
    color: #e06c75
}

.ace-one-dark .ace_variable.ace_parameter {
    color: #d19a66
}

.ace-one-dark .ace_meta.ace_tag {
    color: #e06c75
}

.ace-one-dark .ace_entity.ace_other.ace_attribute-name {
    color: #e06c75
}

.ace-one-dark .ace_entity.ace_name.ace_function {
    color: #61afef
}

.ace-one-dark .ace_entity.ace_name.ace_tag {
    color: #e06c75
}

.ace-one-dark .ace_markup.ace_heading {
    color: #98c379
}

.ace-one-dark .ace_indent-guide {
    background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAEklEQVQImWPQ09NrYAgMjP4PAAtGAwchHMyAAAAAAElFTkSuQmCC) right repeat-y
}

.ace-one-dark .ace_indent-guide-active {
    background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAEklEQVQIW2PQ1dX9zzBz5sz/ABCcBFFentLlAAAAAElFTkSuQmCC) right repeat-y;
}

/*# sourceURL=ace/css/ace-one-dark */</style><style id="ace-cobalt">.ace-cobalt .ace_gutter {
  background: #011e3a;
  color: rgb(128,145,160)
}

.ace-cobalt .ace_print-margin {
  width: 1px;
  background: #555555
}

.ace-cobalt {
  background-color: #002240;
  color: #FFFFFF
}

.ace-cobalt .ace_cursor {
  color: #FFFFFF
}

.ace-cobalt .ace_marker-layer .ace_selection {
  background: rgba(179, 101, 57, 0.75)
}

.ace-cobalt.ace_multiselect .ace_selection.ace_start {
  box-shadow: 0 0 3px 0px #002240;
}

.ace-cobalt .ace_marker-layer .ace_step {
  background: rgb(127, 111, 19)
}

.ace-cobalt .ace_marker-layer .ace_bracket {
  margin: -1px 0 0 -1px;
  border: 1px solid rgba(255, 255, 255, 0.15)
}

.ace-cobalt .ace_marker-layer .ace_active-line {
  background: rgba(0, 0, 0, 0.35)
}

.ace-cobalt .ace_gutter-active-line {
  background-color: rgba(0, 0, 0, 0.35)
}

.ace-cobalt .ace_marker-layer .ace_selected-word {
  border: 1px solid rgba(179, 101, 57, 0.75)
}

.ace-cobalt .ace_invisible {
  color: rgba(255, 255, 255, 0.15)
}

.ace-cobalt .ace_keyword,
.ace-cobalt .ace_meta {
  color: #FF9D00
}

.ace-cobalt .ace_constant,
.ace-cobalt .ace_constant.ace_character,
.ace-cobalt .ace_constant.ace_character.ace_escape,
.ace-cobalt .ace_constant.ace_other {
  color: #FF628C
}

.ace-cobalt .ace_invalid {
  color: #F8F8F8;
  background-color: #800F00
}

.ace-cobalt .ace_support {
  color: #80FFBB
}

.ace-cobalt .ace_support.ace_constant {
  color: #EB939A
}

.ace-cobalt .ace_fold {
  background-color: #FF9D00;
  border-color: #FFFFFF
}

.ace-cobalt .ace_support.ace_function {
  color: #FFB054
}

.ace-cobalt .ace_storage {
  color: #FFEE80
}

.ace-cobalt .ace_entity {
  color: #FFDD00
}

.ace-cobalt .ace_string {
  color: #3AD900
}

.ace-cobalt .ace_string.ace_regexp {
  color: #80FFC2
}

.ace-cobalt .ace_comment {
  font-style: italic;
  color: #0088FF
}

.ace-cobalt .ace_heading,
.ace-cobalt .ace_markup.ace_heading {
  color: #C8E4FD;
  background-color: #001221
}

.ace-cobalt .ace_list,
.ace-cobalt .ace_markup.ace_list {
  background-color: #130D26
}

.ace-cobalt .ace_variable {
  color: #CCCCCC
}

.ace-cobalt .ace_variable.ace_language {
  color: #FF80E1
}

.ace-cobalt .ace_meta.ace_tag {
  color: #9EFFFF
}

.ace-cobalt .ace_indent-guide {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAEklEQVQImWNgYGBgYHCLSvkPAAP3AgSDTRd4AAAAAElFTkSuQmCC) right repeat-y
}

.ace-cobalt .ace_indent-guide-active {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAEklEQVQIW2PQ1dX9zzBz5sz/ABCcBFFentLlAAAAAElFTkSuQmCC) right repeat-y;
}

/*# sourceURL=ace/css/ace-cobalt */</style><style id="ace-dracula">/*
 * Copyright © 2017 Zeno Rocha <hi@zenorocha.com>
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */

.ace-dracula .ace_gutter {
  background: #282a36;
  color: rgb(144,145,148)
}

.ace-dracula .ace_print-margin {
  width: 1px;
  background: #44475a
}

.ace-dracula {
  background-color: #282a36;
  color: #f8f8f2
}

.ace-dracula .ace_cursor {
  color: #f8f8f0
}

.ace-dracula .ace_marker-layer .ace_selection {
  background: #44475a
}

.ace-dracula.ace_multiselect .ace_selection.ace_start {
  box-shadow: 0 0 3px 0px #282a36;
  border-radius: 2px
}

.ace-dracula .ace_marker-layer .ace_step {
  background: rgb(198, 219, 174)
}

.ace-dracula .ace_marker-layer .ace_bracket {
  margin: -1px 0 0 -1px;
  border: 1px solid #a29709
}

.ace-dracula .ace_marker-layer .ace_active-line {
  background: #44475a
}

.ace-dracula .ace_gutter-active-line {
  background-color: #44475a
}

.ace-dracula .ace_marker-layer .ace_selected-word {
  box-shadow: 0px 0px 0px 1px #a29709;
  border-radius: 3px;
}

.ace-dracula .ace_fold {
  background-color: #50fa7b;
  border-color: #f8f8f2
}

.ace-dracula .ace_keyword {
  color: #ff79c6
}

.ace-dracula .ace_constant.ace_language {
  color: #bd93f9
}

.ace-dracula .ace_constant.ace_numeric {
  color: #bd93f9
}

.ace-dracula .ace_constant.ace_character {
  color: #bd93f9
}

.ace-dracula .ace_constant.ace_character.ace_escape {
  color: #ff79c6
}

.ace-dracula .ace_constant.ace_other {
  color: #bd93f9
}

.ace-dracula .ace_support.ace_function {
  color: #8be9fd
}

.ace-dracula .ace_support.ace_constant {
  color: #6be5fd
}

.ace-dracula .ace_support.ace_class {
  font-style: italic;
  color: #66d9ef
}

.ace-dracula .ace_support.ace_type {
  font-style: italic;
  color: #66d9ef
}

.ace-dracula .ace_storage {
  color: #ff79c6
}

.ace-dracula .ace_storage.ace_type {
  font-style: italic;
  color: #8be9fd
}

.ace-dracula .ace_invalid {
  color: #F8F8F0;
  background-color: #ff79c6
}

.ace-dracula .ace_invalid.ace_deprecated {
  color: #F8F8F0;
  background-color: #bd93f9
}

.ace-dracula .ace_string {
  color: #f1fa8c
}

.ace-dracula .ace_comment {
  color: #6272a4
}

.ace-dracula .ace_variable {
  color: #50fa7b
}

.ace-dracula .ace_variable.ace_parameter {
  font-style: italic;
  color: #ffb86c
}

.ace-dracula .ace_entity.ace_other.ace_attribute-name {
  color: #50fa7b
}

.ace-dracula .ace_entity.ace_name.ace_function {
  color: #50fa7b
}

.ace-dracula .ace_entity.ace_name.ace_tag {
  color: #ff79c6
}
.ace-dracula .ace_invisible {
  color: #626680;
}

.ace-dracula .ace_indent-guide {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAEklEQVQImWNgYGBgYHB3d/8PAAOIAdULw8qMAAAAAElFTkSuQmCC) right repeat-y
}

.ace-dracula .ace_indent-guide-active {
  background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACAQMAAACjTyRkAAAABlBMVEUAAADCwsK76u2xAAAAAXRSTlMAQObYZgAAAAxJREFUCNdjYGBoAAAAhACBGFbxzQAAAABJRU5ErkJggg==") right repeat-y;
}

/*# sourceURL=ace/css/ace-dracula */</style><style id="ace-tomorrow-night">.ace-tomorrow-night .ace_gutter {
  background: #25282c;
  color: #C5C8C6
}

.ace-tomorrow-night .ace_print-margin {
  width: 1px;
  background: #25282c
}

.ace-tomorrow-night {
  background-color: #1D1F21;
  color: #C5C8C6
}

.ace-tomorrow-night .ace_cursor {
  color: #AEAFAD
}

.ace-tomorrow-night .ace_marker-layer .ace_selection {
  background: #373B41
}

.ace-tomorrow-night.ace_multiselect .ace_selection.ace_start {
  box-shadow: 0 0 3px 0px #1D1F21;
}

.ace-tomorrow-night .ace_marker-layer .ace_step {
  background: rgb(102, 82, 0)
}

.ace-tomorrow-night .ace_marker-layer .ace_bracket {
  margin: -1px 0 0 -1px;
  border: 1px solid #4B4E55
}

.ace-tomorrow-night .ace_marker-layer .ace_active-line {
  background: #282A2E
}

.ace-tomorrow-night .ace_gutter-active-line {
  background-color: #282A2E
}

.ace-tomorrow-night .ace_marker-layer .ace_selected-word {
  border: 1px solid #373B41
}

.ace-tomorrow-night .ace_invisible {
  color: #4B4E55
}

.ace-tomorrow-night .ace_keyword,
.ace-tomorrow-night .ace_meta,
.ace-tomorrow-night .ace_storage,
.ace-tomorrow-night .ace_storage.ace_type,
.ace-tomorrow-night .ace_support.ace_type {
  color: #B294BB
}

.ace-tomorrow-night .ace_keyword.ace_operator {
  color: #8ABEB7
}

.ace-tomorrow-night .ace_constant.ace_character,
.ace-tomorrow-night .ace_constant.ace_language,
.ace-tomorrow-night .ace_constant.ace_numeric,
.ace-tomorrow-night .ace_keyword.ace_other.ace_unit,
.ace-tomorrow-night .ace_support.ace_constant,
.ace-tomorrow-night .ace_variable.ace_parameter {
  color: #DE935F
}

.ace-tomorrow-night .ace_constant.ace_other {
  color: #CED1CF
}

.ace-tomorrow-night .ace_invalid {
  color: #CED2CF;
  background-color: #DF5F5F
}

.ace-tomorrow-night .ace_invalid.ace_deprecated {
  color: #CED2CF;
  background-color: #B798BF
}

.ace-tomorrow-night .ace_fold {
  background-color: #81A2BE;
  border-color: #C5C8C6
}

.ace-tomorrow-night .ace_entity.ace_name.ace_function,
.ace-tomorrow-night .ace_support.ace_function,
.ace-tomorrow-night .ace_variable {
  color: #81A2BE
}

.ace-tomorrow-night .ace_support.ace_class,
.ace-tomorrow-night .ace_support.ace_type {
  color: #F0C674
}

.ace-tomorrow-night .ace_heading,
.ace-tomorrow-night .ace_markup.ace_heading,
.ace-tomorrow-night .ace_string {
  color: #B5BD68
}

.ace-tomorrow-night .ace_entity.ace_name.ace_tag,
.ace-tomorrow-night .ace_entity.ace_other.ace_attribute-name,
.ace-tomorrow-night .ace_meta.ace_tag,
.ace-tomorrow-night .ace_string.ace_regexp,
.ace-tomorrow-night .ace_variable {
  color: #CC6666
}

.ace-tomorrow-night .ace_comment {
  color: #969896
}

.ace-tomorrow-night .ace_indent-guide {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAEklEQVQImWNgYGBgYHB3d/8PAAOIAdULw8qMAAAAAElFTkSuQmCC) right repeat-y
}

.ace-tomorrow-night .ace_indent-guide-active {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAEklEQVQIW2PQ1dX9zzBz5sz/ABCcBFFentLlAAAAAElFTkSuQmCC) right repeat-y;
}

/*# sourceURL=ace/css/ace-tomorrow-night */</style><style id="ace-solarized-light">.ace-solarized-light .ace_gutter {
  background: #fbf1d3;
  color: #333
}

.ace-solarized-light .ace_print-margin {
  width: 1px;
  background: #e8e8e8
}

.ace-solarized-light {
  background-color: #FDF6E3;
  color: #586E75
}

.ace-solarized-light .ace_cursor {
  color: #000000
}

.ace-solarized-light .ace_marker-layer .ace_selection {
  background: rgba(7, 54, 67, 0.09)
}

.ace-solarized-light.ace_multiselect .ace_selection.ace_start {
  box-shadow: 0 0 3px 0px #FDF6E3;
}

.ace-solarized-light .ace_marker-layer .ace_step {
  background: rgb(255, 255, 0)
}

.ace-solarized-light .ace_marker-layer .ace_bracket {
  margin: -1px 0 0 -1px;
  border: 1px solid rgba(147, 161, 161, 0.50)
}

.ace-solarized-light .ace_marker-layer .ace_active-line {
  background: #EEE8D5
}

.ace-solarized-light .ace_gutter-active-line {
  background-color : #EDE5C1
}

.ace-solarized-light .ace_marker-layer .ace_selected-word {
  border: 1px solid #7f9390
}

.ace-solarized-light .ace_invisible {
  color: rgba(147, 161, 161, 0.50)
}

.ace-solarized-light .ace_keyword,
.ace-solarized-light .ace_meta,
.ace-solarized-light .ace_support.ace_class,
.ace-solarized-light .ace_support.ace_type {
  color: #859900
}

.ace-solarized-light .ace_constant.ace_character,
.ace-solarized-light .ace_constant.ace_other {
  color: #CB4B16
}

.ace-solarized-light .ace_constant.ace_language {
  color: #B58900
}

.ace-solarized-light .ace_constant.ace_numeric {
  color: #D33682
}

.ace-solarized-light .ace_fold {
  background-color: #268BD2;
  border-color: #586E75
}

.ace-solarized-light .ace_entity.ace_name.ace_function,
.ace-solarized-light .ace_entity.ace_name.ace_tag,
.ace-solarized-light .ace_support.ace_function,
.ace-solarized-light .ace_variable,
.ace-solarized-light .ace_variable.ace_language {
  color: #268BD2
}

.ace-solarized-light .ace_storage {
  color: #073642
}

.ace-solarized-light .ace_string {
  color: #2AA198
}

.ace-solarized-light .ace_string.ace_regexp {
  color: #D30102
}

.ace-solarized-light .ace_comment,
.ace-solarized-light .ace_entity.ace_other.ace_attribute-name {
  color: #93A1A1
}

.ace-solarized-light .ace_indent-guide {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAEklEQVQImWNgYGBgYHjy8NJ/AAjgA5fzQUmBAAAAAElFTkSuQmCC) right repeat-y
}

.ace-solarized-light .ace_indent-guide-active {
  background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAIGNIUk0AAHolAACAgwAA+f8AAIDpAAB1MAAA6mAAADqYAAAXb5JfxUYAAAAZSURBVHjaYvj///9/hivKyv8BAAAA//8DACLqBhbvk+/eAAAAAElFTkSuQmCC") right repeat-y;
} 

/*# sourceURL=ace/css/ace-solarized-light */</style><style id="ace-solarized-dark">.ace-solarized-dark .ace_gutter {
  background: #01313f;
  color: #d0edf7
}

.ace-solarized-dark .ace_print-margin {
  width: 1px;
  background: #33555E
}

.ace-solarized-dark {
  background-color: #002B36;
  color: #839496
}

.ace-solarized-dark .ace_entity.ace_other.ace_attribute-name,
.ace-solarized-dark .ace_storage {
  color: #839496
}

.ace-solarized-dark .ace_cursor,
.ace-solarized-dark .ace_string.ace_regexp {
  color: #D30102
}

.ace-solarized-dark .ace_marker-layer .ace_active-line,
.ace-solarized-dark .ace_marker-layer .ace_selection {
  background: rgba(255, 255, 255, 0.1)
}

.ace-solarized-dark.ace_multiselect .ace_selection.ace_start {
  box-shadow: 0 0 3px 0px #002B36;
}

.ace-solarized-dark .ace_marker-layer .ace_step {
  background: rgb(102, 82, 0)
}

.ace-solarized-dark .ace_marker-layer .ace_bracket {
  margin: -1px 0 0 -1px;
  border: 1px solid rgba(147, 161, 161, 0.50)
}

.ace-solarized-dark .ace_gutter-active-line {
  background-color: #0d3440
}

.ace-solarized-dark .ace_marker-layer .ace_selected-word {
  border: 1px solid #073642
}

.ace-solarized-dark .ace_invisible {
  color: rgba(147, 161, 161, 0.50)
}

.ace-solarized-dark .ace_keyword,
.ace-solarized-dark .ace_meta,
.ace-solarized-dark .ace_support.ace_class,
.ace-solarized-dark .ace_support.ace_type {
  color: #859900
}

.ace-solarized-dark .ace_constant.ace_character,
.ace-solarized-dark .ace_constant.ace_other {
  color: #CB4B16
}

.ace-solarized-dark .ace_constant.ace_language {
  color: #B58900
}

.ace-solarized-dark .ace_constant.ace_numeric {
  color: #D33682
}

.ace-solarized-dark .ace_fold {
  background-color: #268BD2;
  border-color: #93A1A1
}

.ace-solarized-dark .ace_entity.ace_name.ace_function,
.ace-solarized-dark .ace_entity.ace_name.ace_tag,
.ace-solarized-dark .ace_support.ace_function,
.ace-solarized-dark .ace_variable,
.ace-solarized-dark .ace_variable.ace_language {
  color: #268BD2
}

.ace-solarized-dark .ace_string {
  color: #2AA198
}

.ace-solarized-dark .ace_comment {
  font-style: italic;
  color: #657B83
}

.ace-solarized-dark .ace_indent-guide {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAEklEQVQImWNg0Db1ZVCxc/sPAAd4AlUHlLenAAAAAElFTkSuQmCC) right repeat-y
}

.ace-solarized-dark .ace_indent-guide-active {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAEklEQVQIW2PQ1dX9zzBz5sz/ABCcBFFentLlAAAAAElFTkSuQmCC) right repeat-y;
}

/*# sourceURL=ace/css/ace-solarized-dark */</style><style id="ace-eclipse">.ace-eclipse .ace_gutter {
  background: #ebebeb;
  border-right: 1px solid rgb(159, 159, 159);
  color: rgb(136, 136, 136);
}

.ace-eclipse .ace_print-margin {
  width: 1px;
  background: #ebebeb;
}

.ace-eclipse {
  background-color: #FFFFFF;
  color: black;
}

.ace-eclipse .ace_fold {
    background-color: rgb(60, 76, 114);
}

.ace-eclipse .ace_cursor {
  color: black;
}

.ace-eclipse .ace_storage,
.ace-eclipse .ace_keyword,
.ace-eclipse .ace_variable {
  color: rgb(127, 0, 85);
}

.ace-eclipse .ace_constant.ace_buildin {
  color: rgb(88, 72, 246);
}

.ace-eclipse .ace_constant.ace_library {
  color: rgb(6, 150, 14);
}

.ace-eclipse .ace_function {
  color: rgb(60, 76, 114);
}

.ace-eclipse .ace_string {
  color: rgb(42, 0, 255);
}

.ace-eclipse .ace_comment {
  color: rgb(113, 150, 130);
}

.ace-eclipse .ace_comment.ace_doc {
  color: rgb(63, 95, 191);
}

.ace-eclipse .ace_comment.ace_doc.ace_tag {
  color: rgb(127, 159, 191);
}

.ace-eclipse .ace_constant.ace_numeric {
  color: darkblue;
}

.ace-eclipse .ace_tag {
  color: rgb(25, 118, 116);
}

.ace-eclipse .ace_type {
  color: rgb(127, 0, 127);
}

.ace-eclipse .ace_xml-pe {
  color: rgb(104, 104, 91);
}

.ace-eclipse .ace_marker-layer .ace_selection {
  background: rgb(181, 213, 255);
}

.ace-eclipse .ace_marker-layer .ace_bracket {
  margin: -1px 0 0 -1px;
  border: 1px solid rgb(192, 192, 192);
}

.ace-eclipse .ace_meta.ace_tag {
  color:rgb(25, 118, 116);
}

.ace-eclipse .ace_invisible {
  color: #ddd;
}

.ace-eclipse .ace_entity.ace_other.ace_attribute-name {
  color:rgb(127, 0, 127);
}
.ace-eclipse .ace_marker-layer .ace_step {
  background: rgb(255, 255, 0);
}

.ace-eclipse .ace_active-line {
  background: rgb(232, 242, 254);
}

.ace-eclipse .ace_gutter-active-line {
  background-color : #DADADA;
}

.ace-eclipse .ace_marker-layer .ace_selected-word {
  border: 1px solid rgb(181, 213, 255);
}

.ace-eclipse .ace_indent-guide {
  background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bLly//BwAmVgd1/w11/gAAAABJRU5ErkJggg==") right repeat-y;
}

.ace-eclipse .ace_indent-guide-active {
  background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAIGNIUk0AAHolAACAgwAA+f8AAIDpAAB1MAAA6mAAADqYAAAXb5JfxUYAAAAZSURBVHjaYvj///9/hivKyv8BAAAA//8DACLqBhbvk+/eAAAAAElFTkSuQmCC") right repeat-y;
} 

/*# sourceURL=ace/css/ace-eclipse */</style><style id="ace-xcode">/* THIS THEME WAS AUTOGENERATED BY Theme.tmpl.css (UUID: EE3AD170-2B7F-4DE1-B724-C75F13FE0085) */

.ace-xcode .ace_gutter {
  background: #e8e8e8;
  color: #333
}

.ace-xcode .ace_print-margin {
  width: 1px;
  background: #e8e8e8
}

.ace-xcode {
  background-color: #FFFFFF;
  color: #000000
}

.ace-xcode .ace_cursor {
  color: #000000
}

.ace-xcode .ace_marker-layer .ace_selection {
  background: #B5D5FF
}

.ace-xcode.ace_multiselect .ace_selection.ace_start {
  box-shadow: 0 0 3px 0px #FFFFFF;
}

.ace-xcode .ace_marker-layer .ace_step {
  background: rgb(198, 219, 174)
}

.ace-xcode .ace_marker-layer .ace_bracket {
  margin: -1px 0 0 -1px;
  border: 1px solid #BFBFBF
}

.ace-xcode .ace_marker-layer .ace_active-line {
  background: rgba(0, 0, 0, 0.071)
}

.ace-xcode .ace_gutter-active-line {
  background-color: rgba(0, 0, 0, 0.071)
}

.ace-xcode .ace_marker-layer .ace_selected-word {
  border: 1px solid #B5D5FF
}

.ace-xcode .ace_constant.ace_language,
.ace-xcode .ace_keyword,
.ace-xcode .ace_meta,
.ace-xcode .ace_variable.ace_language {
  color: #C800A4
}

.ace-xcode .ace_invisible {
  color: #BFBFBF
}

.ace-xcode .ace_constant.ace_character,
.ace-xcode .ace_constant.ace_other {
  color: #275A5E
}

.ace-xcode .ace_constant.ace_numeric {
  color: #3A00DC
}

.ace-xcode .ace_entity.ace_other.ace_attribute-name,
.ace-xcode .ace_support.ace_constant,
.ace-xcode .ace_support.ace_function {
  color: #450084
}

.ace-xcode .ace_fold {
  background-color: #C800A4;
  border-color: #000000
}

.ace-xcode .ace_entity.ace_name.ace_tag,
.ace-xcode .ace_support.ace_class,
.ace-xcode .ace_support.ace_type {
  color: #790EAD
}

.ace-xcode .ace_storage {
  color: #C900A4
}

.ace-xcode .ace_string {
  color: #DF0002
}

.ace-xcode .ace_comment {
  color: #008E00
}

.ace-xcode .ace_indent-guide {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bLly//BwAmVgd1/w11/gAAAABJRU5ErkJggg==) right repeat-y
}

.ace-xcode .ace_indent-guide-active {
  background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAIGNIUk0AAHolAACAgwAA+f8AAIDpAAB1MAAA6mAAADqYAAAXb5JfxUYAAAAZSURBVHjaYvj///9/hivKyv8BAAAA//8DACLqBhbvk+/eAAAAAElFTkSuQmCC") right repeat-y;
} 

/*# sourceURL=ace/css/ace-xcode */</style><style id="ace-monokai">.ace-monokai .ace_gutter {
  background: #2F3129;
  color: #8F908A
}

.ace-monokai .ace_print-margin {
  width: 1px;
  background: #555651
}

.ace-monokai {
  background-color: #272822;
  color: #F8F8F2
}

.ace-monokai .ace_cursor {
  color: #F8F8F0
}

.ace-monokai .ace_marker-layer .ace_selection {
  background: #49483E
}

.ace-monokai.ace_multiselect .ace_selection.ace_start {
  box-shadow: 0 0 3px 0px #272822;
}

.ace-monokai .ace_marker-layer .ace_step {
  background: rgb(102, 82, 0)
}

.ace-monokai .ace_marker-layer .ace_bracket {
  margin: -1px 0 0 -1px;
  border: 1px solid #49483E
}

.ace-monokai .ace_marker-layer .ace_active-line {
  background: #202020
}

.ace-monokai .ace_gutter-active-line {
  background-color: #272727
}

.ace-monokai .ace_marker-layer .ace_selected-word {
  border: 1px solid #49483E
}

.ace-monokai .ace_invisible {
  color: #52524d
}

.ace-monokai .ace_entity.ace_name.ace_tag,
.ace-monokai .ace_keyword,
.ace-monokai .ace_meta.ace_tag,
.ace-monokai .ace_storage {
  color: #F92672
}

.ace-monokai .ace_punctuation,
.ace-monokai .ace_punctuation.ace_tag {
  color: #fff
}

.ace-monokai .ace_constant.ace_character,
.ace-monokai .ace_constant.ace_language,
.ace-monokai .ace_constant.ace_numeric,
.ace-monokai .ace_constant.ace_other {
  color: #AE81FF
}

.ace-monokai .ace_invalid {
  color: #F8F8F0;
  background-color: #F92672
}

.ace-monokai .ace_invalid.ace_deprecated {
  color: #F8F8F0;
  background-color: #AE81FF
}

.ace-monokai .ace_support.ace_constant,
.ace-monokai .ace_support.ace_function {
  color: #66D9EF
}

.ace-monokai .ace_fold {
  background-color: #A6E22E;
  border-color: #F8F8F2
}

.ace-monokai .ace_storage.ace_type,
.ace-monokai .ace_support.ace_class,
.ace-monokai .ace_support.ace_type {
  font-style: italic;
  color: #66D9EF
}

.ace-monokai .ace_entity.ace_name.ace_function,
.ace-monokai .ace_entity.ace_other,
.ace-monokai .ace_entity.ace_other.ace_attribute-name,
.ace-monokai .ace_variable {
  color: #A6E22E
}

.ace-monokai .ace_variable.ace_parameter {
  font-style: italic;
  color: #FD971F
}

.ace-monokai .ace_string {
  color: #E6DB74
}

.ace-monokai .ace_comment {
  color: #75715E
}

.ace-monokai .ace_indent-guide {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAEklEQVQImWPQ0FD0ZXBzd/wPAAjVAoxeSgNeAAAAAElFTkSuQmCC) right repeat-y
}

.ace-monokai .ace_indent-guide-active {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAEklEQVQIW2PQ1dX9zzBz5sz/ABCcBFFentLlAAAAAElFTkSuQmCC) right repeat-y;
}

/*# sourceURL=ace/css/ace-monokai */</style><style id="autocompletion.css">
.ace_editor.ace_autocomplete .ace_marker-layer .ace_active-line {
    background-color: #CAD6FA;
    z-index: 1;
}
.ace_dark.ace_editor.ace_autocomplete .ace_marker-layer .ace_active-line {
    background-color: #3a674e;
}
.ace_editor.ace_autocomplete .ace_line-hover {
    border: 1px solid #abbffe;
    margin-top: -1px;
    background: rgba(233,233,253,0.4);
    position: absolute;
    z-index: 2;
}
.ace_dark.ace_editor.ace_autocomplete .ace_line-hover {
    border: 1px solid rgba(109, 150, 13, 0.8);
    background: rgba(58, 103, 78, 0.62);
}
.ace_completion-meta {
    opacity: 0.5;
    margin-left: 0.9em;
}
.ace_completion-message {
    margin-left: 0.9em;
    color: blue;
}
.ace_editor.ace_autocomplete .ace_completion-highlight{
    color: #2d69c7;
}
.ace_dark.ace_editor.ace_autocomplete .ace_completion-highlight{
    color: #93ca12;
}
.ace_editor.ace_autocomplete {
    width: 300px;
    z-index: 200000;
    border: 1px lightgray solid;
    position: fixed;
    box-shadow: 2px 3px 5px rgba(0,0,0,.2);
    line-height: 1.4;
    background: #fefefe;
    color: #111;
}
.ace_dark.ace_editor.ace_autocomplete {
    border: 1px #484747 solid;
    box-shadow: 2px 3px 5px rgba(0, 0, 0, 0.51);
    line-height: 1.4;
    background: #25282c;
    color: #c1c1c1;
}
.ace_autocomplete .ace_text-layer  {
    width: calc(100% - 8px);
}
.ace_autocomplete .ace_line {
    display: flex;
    align-items: center;
}
.ace_autocomplete .ace_line > * {
    min-width: 0;
    flex: 0 0 auto;
}
.ace_autocomplete .ace_line .ace_ {
    flex: 0 1 auto;
    overflow: hidden;
    text-overflow: ellipsis;
}
.ace_autocomplete .ace_completion-spacer {
    flex: 1;
}
.ace_autocomplete.ace_loading:after  {
    content: "";
    position: absolute;
    top: 0px;
    height: 2px;
    width: 8%;
    background: blue;
    z-index: 100;
    animation: ace_progress 3s infinite linear;
    animation-delay: 300ms;
    transform: translateX(-100%) scaleX(1);
}
@keyframes ace_progress {
    0% { transform: translateX(-100%) scaleX(1) }
    50% { transform: translateX(625%) scaleX(2) } 
    100% { transform: translateX(1500%) scaleX(3) } 
}
@media (prefers-reduced-motion) {
    .ace_autocomplete.ace_loading:after {
        transform: translateX(625%) scaleX(2);
        animation: none;
     }
}

/*# sourceURL=ace/css/autocompletion.css */</style><style id="snippets.css">
.ace_snippet-marker {
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    background: rgba(194, 193, 208, 0.09);
    border: 1px dotted rgba(211, 208, 235, 0.62);
    position: absolute;
}
/*# sourceURL=ace/css/snippets.css */</style><style id="error_marker.css">
    .error_widget_wrapper {
        background: inherit;
        color: inherit;
        border:none
    }
    .error_widget {
        border-top: solid 2px;
        border-bottom: solid 2px;
        margin: 5px 0;
        padding: 10px 40px;
        white-space: pre-wrap;
    }
    .error_widget.ace_error, .error_widget_arrow.ace_error{
        border-color: #ff5a5a
    }
    .error_widget.ace_warning, .error_widget_arrow.ace_warning{
        border-color: #F1D817
    }
    .error_widget.ace_info, .error_widget_arrow.ace_info{
        border-color: #5a5a5a
    }
    .error_widget.ace_ok, .error_widget_arrow.ace_ok{
        border-color: #5aaa5a
    }
    .error_widget_arrow {
        position: absolute;
        border: solid 5px;
        border-top-color: transparent!important;
        border-right-color: transparent!important;
        border-left-color: transparent!important;
        top: -5px;
    }

/*# sourceURL=ace/css/error_marker.css */</style><style id="ace-tm">.ace-tm .ace_gutter {
  background: #f0f0f0;
  color: #333;
}

.ace-tm .ace_print-margin {
  width: 1px;
  background: #e8e8e8;
}

.ace-tm .ace_fold {
    background-color: #6B72E6;
}

.ace-tm {
  background-color: #FFFFFF;
  color: black;
}

.ace-tm .ace_cursor {
  color: black;
}
        
.ace-tm .ace_invisible {
  color: rgb(191, 191, 191);
}

.ace-tm .ace_storage,
.ace-tm .ace_keyword {
  color: blue;
}

.ace-tm .ace_constant {
  color: rgb(197, 6, 11);
}

.ace-tm .ace_constant.ace_buildin {
  color: rgb(88, 72, 246);
}

.ace-tm .ace_constant.ace_language {
  color: rgb(88, 92, 246);
}

.ace-tm .ace_constant.ace_library {
  color: rgb(6, 150, 14);
}

.ace-tm .ace_invalid {
  background-color: rgba(255, 0, 0, 0.1);
  color: red;
}

.ace-tm .ace_support.ace_function {
  color: rgb(60, 76, 114);
}

.ace-tm .ace_support.ace_constant {
  color: rgb(6, 150, 14);
}

.ace-tm .ace_support.ace_type,
.ace-tm .ace_support.ace_class {
  color: rgb(109, 121, 222);
}

.ace-tm .ace_keyword.ace_operator {
  color: rgb(104, 118, 135);
}

.ace-tm .ace_string {
  color: rgb(3, 106, 7);
}

.ace-tm .ace_comment {
  color: rgb(76, 136, 107);
}

.ace-tm .ace_comment.ace_doc {
  color: rgb(0, 102, 255);
}

.ace-tm .ace_comment.ace_doc.ace_tag {
  color: rgb(128, 159, 191);
}

.ace-tm .ace_constant.ace_numeric {
  color: rgb(0, 0, 205);
}

.ace-tm .ace_variable {
  color: rgb(49, 132, 149);
}

.ace-tm .ace_xml-pe {
  color: rgb(104, 104, 91);
}

.ace-tm .ace_entity.ace_name.ace_function {
  color: #0000A2;
}


.ace-tm .ace_heading {
  color: rgb(12, 7, 255);
}

.ace-tm .ace_list {
  color:rgb(185, 6, 144);
}

.ace-tm .ace_meta.ace_tag {
  color:rgb(0, 22, 142);
}

.ace-tm .ace_string.ace_regex {
  color: rgb(255, 0, 0)
}

.ace-tm .ace_marker-layer .ace_selection {
  background: rgb(181, 213, 255);
}
.ace-tm.ace_multiselect .ace_selection.ace_start {
  box-shadow: 0 0 3px 0px white;
}
.ace-tm .ace_marker-layer .ace_step {
  background: rgb(252, 255, 0);
}

.ace-tm .ace_marker-layer .ace_stack {
  background: rgb(164, 229, 101);
}

.ace-tm .ace_marker-layer .ace_bracket {
  margin: -1px 0 0 -1px;
  border: 1px solid rgb(192, 192, 192);
}

.ace-tm .ace_marker-layer .ace_active-line {
  background: rgba(0, 0, 0, 0.07);
}

.ace-tm .ace_gutter-active-line {
    background-color : #dcdcdc;
}

.ace-tm .ace_marker-layer .ace_selected-word {
  background: rgb(250, 250, 255);
  border: 1px solid rgb(200, 200, 250);
}

.ace-tm .ace_indent-guide {
  background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bLly//BwAmVgd1/w11/gAAAABJRU5ErkJggg==") right repeat-y;
}

.ace-tm .ace_indent-guide-active {
  background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAIGNIUk0AAHolAACAgwAA+f8AAIDpAAB1MAAA6mAAADqYAAAXb5JfxUYAAAAZSURBVHjaYvj///9/hivKyv8BAAAA//8DACLqBhbvk+/eAAAAAElFTkSuQmCC") right repeat-y;
}

/*# sourceURL=ace/css/ace-tm */</style><style id="ace_editor.css">
.ace_br1 {border-top-left-radius    : 3px;}
.ace_br2 {border-top-right-radius   : 3px;}
.ace_br3 {border-top-left-radius    : 3px; border-top-right-radius:    3px;}
.ace_br4 {border-bottom-right-radius: 3px;}
.ace_br5 {border-top-left-radius    : 3px; border-bottom-right-radius: 3px;}
.ace_br6 {border-top-right-radius   : 3px; border-bottom-right-radius: 3px;}
.ace_br7 {border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-right-radius: 3px;}
.ace_br8 {border-bottom-left-radius : 3px;}
.ace_br9 {border-top-left-radius    : 3px; border-bottom-left-radius:  3px;}
.ace_br10{border-top-right-radius   : 3px; border-bottom-left-radius:  3px;}
.ace_br11{border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-left-radius:  3px;}
.ace_br12{border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}
.ace_br13{border-top-left-radius    : 3px; border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}
.ace_br14{border-top-right-radius   : 3px; border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}
.ace_br15{border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;}


.ace_editor {
    position: relative;
    overflow: hidden;
    padding: 0;
    font: 12px/normal 'Monaco', 'Menlo', 'Ubuntu Mono', 'Consolas', 'Source Code Pro', 'source-code-pro', monospace;
    direction: ltr;
    text-align: left;
    -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}

.ace_scroller {
    position: absolute;
    overflow: hidden;
    top: 0;
    bottom: 0;
    background-color: inherit;
    -ms-user-select: none;
    -moz-user-select: none;
    -webkit-user-select: none;
    user-select: none;
    cursor: text;
}

.ace_content {
    position: absolute;
    box-sizing: border-box;
    min-width: 100%;
    contain: style size layout;
    font-variant-ligatures: no-common-ligatures;
}

.ace_keyboard-focus:focus {
    box-shadow: inset 0 0 0 2px #5E9ED6;
    outline: none;
}

.ace_dragging .ace_scroller:before{
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    content: '';
    background: rgba(250, 250, 250, 0.01);
    z-index: 1000;
}
.ace_dragging.ace_dark .ace_scroller:before{
    background: rgba(0, 0, 0, 0.01);
}

.ace_gutter {
    position: absolute;
    overflow : hidden;
    width: auto;
    top: 0;
    bottom: 0;
    left: 0;
    cursor: default;
    z-index: 4;
    -ms-user-select: none;
    -moz-user-select: none;
    -webkit-user-select: none;
    user-select: none;
    contain: style size layout;
}

.ace_gutter-active-line {
    position: absolute;
    left: 0;
    right: 0;
}

.ace_scroller.ace_scroll-left:after {
    content: "";
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    box-shadow: 17px 0 16px -16px rgba(0, 0, 0, 0.4) inset;
    pointer-events: none;
}

.ace_gutter-cell, .ace_gutter-cell_svg-icons {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    padding-left: 19px;
    padding-right: 6px;
    background-repeat: no-repeat;
}

.ace_gutter-cell_svg-icons .ace_gutter_annotation {
    margin-left: -14px;
    float: left;
}

.ace_gutter-cell .ace_gutter_annotation {
    margin-left: -19px;
    float: left;
}

.ace_gutter-cell.ace_error, .ace_icon.ace_error, .ace_icon.ace_error_fold {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAABOFBMVEX/////////QRswFAb/Ui4wFAYwFAYwFAaWGAfDRymzOSH/PxswFAb/SiUwFAYwFAbUPRvjQiDllog5HhHdRybsTi3/Tyv9Tir+Syj/UC3////XurebMBIwFAb/RSHbPx/gUzfdwL3kzMivKBAwFAbbvbnhPx66NhowFAYwFAaZJg8wFAaxKBDZurf/RB6mMxb/SCMwFAYwFAbxQB3+RB4wFAb/Qhy4Oh+4QifbNRcwFAYwFAYwFAb/QRzdNhgwFAYwFAbav7v/Uy7oaE68MBK5LxLewr/r2NXewLswFAaxJw4wFAbkPRy2PyYwFAaxKhLm1tMwFAazPiQwFAaUGAb/QBrfOx3bvrv/VC/maE4wFAbRPBq6MRO8Qynew8Dp2tjfwb0wFAbx6eju5+by6uns4uH9/f36+vr/GkHjAAAAYnRSTlMAGt+64rnWu/bo8eAA4InH3+DwoN7j4eLi4xP99Nfg4+b+/u9B/eDs1MD1mO7+4PHg2MXa347g7vDizMLN4eG+Pv7i5evs/v79yu7S3/DV7/498Yv24eH+4ufQ3Ozu/v7+y13sRqwAAADLSURBVHjaZc/XDsFgGIBhtDrshlitmk2IrbHFqL2pvXf/+78DPokj7+Fz9qpU/9UXJIlhmPaTaQ6QPaz0mm+5gwkgovcV6GZzd5JtCQwgsxoHOvJO15kleRLAnMgHFIESUEPmawB9ngmelTtipwwfASilxOLyiV5UVUyVAfbG0cCPHig+GBkzAENHS0AstVF6bacZIOzgLmxsHbt2OecNgJC83JERmePUYq8ARGkJx6XtFsdddBQgZE2nPR6CICZhawjA4Fb/chv+399kfR+MMMDGOQAAAABJRU5ErkJggg==");
    background-repeat: no-repeat;
    background-position: 2px center;
}

.ace_gutter-cell.ace_warning, .ace_icon.ace_warning, .ace_icon.ace_warning_fold {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAmVBMVEX///8AAAD///8AAAAAAABPSzb/5sAAAAB/blH/73z/ulkAAAAAAAD85pkAAAAAAAACAgP/vGz/rkDerGbGrV7/pkQICAf////e0IsAAAD/oED/qTvhrnUAAAD/yHD/njcAAADuv2r/nz//oTj/p064oGf/zHAAAAA9Nir/tFIAAAD/tlTiuWf/tkIAAACynXEAAAAAAAAtIRW7zBpBAAAAM3RSTlMAABR1m7RXO8Ln31Z36zT+neXe5OzooRDfn+TZ4p3h2hTf4t3k3ucyrN1K5+Xaks52Sfs9CXgrAAAAjklEQVR42o3PbQ+CIBQFYEwboPhSYgoYunIqqLn6/z8uYdH8Vmdnu9vz4WwXgN/xTPRD2+sgOcZjsge/whXZgUaYYvT8QnuJaUrjrHUQreGczuEafQCO/SJTufTbroWsPgsllVhq3wJEk2jUSzX3CUEDJC84707djRc5MTAQxoLgupWRwW6UB5fS++NV8AbOZgnsC7BpEAAAAABJRU5ErkJggg==");
    background-repeat: no-repeat;
    background-position: 2px center;
}

.ace_gutter-cell.ace_info, .ace_icon.ace_info {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAAAAAA6mKC9AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAJ0Uk5TAAB2k804AAAAPklEQVQY02NgIB68QuO3tiLznjAwpKTgNyDbMegwisCHZUETUZV0ZqOquBpXj2rtnpSJT1AEnnRmL2OgGgAAIKkRQap2htgAAAAASUVORK5CYII=");
    background-repeat: no-repeat;
    background-position: 2px center;
}
.ace_dark .ace_gutter-cell.ace_info, .ace_dark .ace_icon.ace_info {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAAJFBMVEUAAAChoaGAgIAqKiq+vr6tra1ZWVmUlJSbm5s8PDxubm56enrdgzg3AAAAAXRSTlMAQObYZgAAAClJREFUeNpjYMAPdsMYHegyJZFQBlsUlMFVCWUYKkAZMxZAGdxlDMQBAG+TBP4B6RyJAAAAAElFTkSuQmCC");
}

.ace_icon_svg.ace_error {
    -webkit-mask-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMCAxNiI+CjxnIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlPSJyZWQiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KPGNpcmNsZSBmaWxsPSJub25lIiBjeD0iOCIgY3k9IjgiIHI9IjciIHN0cm9rZS1saW5lam9pbj0icm91bmQiLz4KPGxpbmUgeDE9IjExIiB5MT0iNSIgeDI9IjUiIHkyPSIxMSIvPgo8bGluZSB4MT0iMTEiIHkxPSIxMSIgeDI9IjUiIHkyPSI1Ii8+CjwvZz4KPC9zdmc+");
    background-color: crimson;
}
.ace_icon_svg.ace_warning {
    -webkit-mask-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMCAxNiI+CjxnIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlPSJkYXJrb3JhbmdlIiBzaGFwZS1yZW5kZXJpbmc9Imdlb21ldHJpY1ByZWNpc2lvbiI+Cjxwb2x5Z29uIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGZpbGw9Im5vbmUiIHBvaW50cz0iOCAxIDE1IDE1IDEgMTUgOCAxIi8+CjxyZWN0IHg9IjgiIHk9IjEyIiB3aWR0aD0iMC4wMSIgaGVpZ2h0PSIwLjAxIi8+CjxsaW5lIHgxPSI4IiB5MT0iNiIgeDI9IjgiIHkyPSIxMCIvPgo8L2c+Cjwvc3ZnPg==");
    background-color: darkorange;
}
.ace_icon_svg.ace_info {
    -webkit-mask-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMCAxNiI+CjxnIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlPSJibHVlIiBzaGFwZS1yZW5kZXJpbmc9Imdlb21ldHJpY1ByZWNpc2lvbiI+CjxjaXJjbGUgZmlsbD0ibm9uZSIgY3g9IjgiIGN5PSI4IiByPSI3IiBzdHJva2UtbGluZWpvaW49InJvdW5kIi8+Cjxwb2x5bGluZSBwb2ludHM9IjggMTEgOCA4Ii8+Cjxwb2x5bGluZSBwb2ludHM9IjkgOCA2IDgiLz4KPGxpbmUgeDE9IjEwIiB5MT0iMTEiIHgyPSI2IiB5Mj0iMTEiLz4KPHJlY3QgeD0iOCIgeT0iNSIgd2lkdGg9IjAuMDEiIGhlaWdodD0iMC4wMSIvPgo8L2c+Cjwvc3ZnPg==");
    background-color: royalblue;
}

.ace_icon_svg.ace_error_fold {
    -webkit-mask-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMCAxNiIgZmlsbD0ibm9uZSI+CiAgPHBhdGggZD0ibSAxOC45Mjk4NTEsNy44Mjk4MDc2IGMgMC4xNDYzNTMsNi4zMzc0NjA0IC02LjMyMzE0Nyw3Ljc3Nzg0NDQgLTcuNDc3OTEyLDcuNzc3ODQ0NCAtMi4xMDcyNzI2LC0wLjEyODc1IDUuMTE3Njc4LDAuMzU2MjQ5IDUuMDUxNjk4LC03Ljg3MDA2MTggLTAuNjA0NjcyLC04LjAwMzk3MzQ5IC03LjA3NzI3MDYsLTcuNTYzMTE4OSAtNC44NTczLC03LjQzMDM5NTU2IDEuNjA2LC0wLjExNTE0MjI1IDYuODk3NDg1LDEuMjYyNTQ1OTYgNy4yODM1MTQsNy41MjI2MTI5NiB6IiBmaWxsPSJjcmltc29uIiBzdHJva2Utd2lkdGg9IjIiLz4KICA8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0ibSA4LjExNDc1NjIsMi4wNTI5ODI4IGMgMy4zNDkxNjk4LDAgNi4wNjQxMzI4LDIuNjc2ODYyNyA2LjA2NDEzMjgsNS45Nzg5NTMgMCwzLjMwMjExMjIgLTIuNzE0OTYzLDUuOTc4OTIwMiAtNi4wNjQxMzI4LDUuOTc4OTIwMiAtMy4zNDkxNDczLDAgLTYuMDY0MTc3MiwtMi42NzY4MDggLTYuMDY0MTc3MiwtNS45Nzg5MjAyIDAuMDA1MzksLTMuMjk5ODg2MSAyLjcxNzI2NTYsLTUuOTczNjQwOCA2LjA2NDE3NzIsLTUuOTc4OTUzIHogbSAwLC0xLjczNTgyNzE5IGMgLTQuMzIxNDgzNiwwIC03LjgyNDc0MDM4LDMuNDU0MDE4NDkgLTcuODI0NzQwMzgsNy43MTQ3ODAxOSAwLDQuMjYwNzI4MiAzLjUwMzI1Njc4LDcuNzE0NzQ1MiA3LjgyNDc0MDM4LDcuNzE0NzQ1MiA0LjMyMTQ0OTgsMCA3LjgyNDY5OTgsLTMuNDU0MDE3IDcuODI0Njk5OCwtNy43MTQ3NDUyIDAsLTIuMDQ2MDkxNCAtMC44MjQzOTIsLTQuMDA4MzY3MiAtMi4yOTE3NTYsLTUuNDU1MTc0NiBDIDEyLjE4MDIyNSwxLjEyOTk2NDggMTAuMTkwMDEzLDAuMzE3MTU1NjEgOC4xMTQ3NTYyLDAuMzE3MTU1NjEgWiBNIDYuOTM3NDU2Myw4LjI0MDU5ODUgNC42NzE4Njg1LDEwLjQ4NTg1MiA2LjAwODY4MTQsMTEuODc2NzI4IDguMzE3MDAzNSw5LjYwMDc5MTEgMTAuNjI1MzM3LDExLjg3NjcyOCAxMS45NjIxMzgsMTAuNDg1ODUyIDkuNjk2NTUwOCw4LjI0MDU5ODUgMTEuOTYyMTM4LDYuMDA2ODA2NiAxMC41NzMyNDYsNC42Mzc0MzM1IDguMzE3MDAzNSw2Ljg3MzQyOTcgNi4wNjA3NjA3LDQuNjM3NDMzNSA0LjY3MTg2ODUsNi4wMDY4MDY2IFoiIGZpbGw9ImNyaW1zb24iIHN0cm9rZS13aWR0aD0iMiIvPgo8L3N2Zz4=");
    background-color: crimson;
}
.ace_icon_svg.ace_warning_fold {
    -webkit-mask-image: url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAyMCAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xNC43NzY5IDE0LjczMzdMOC42NTE5MiAyLjQ4MzY5QzguMzI5NDYgMS44Mzg3NyA3LjQwOTEzIDEuODM4NzcgNy4wODY2NyAyLjQ4MzY5TDAuOTYxNjY5IDE0LjczMzdDMC42NzA3NzUgMTUuMzE1NSAxLjA5MzgzIDE2IDEuNzQ0MjkgMTZIMTMuOTk0M0MxNC42NDQ4IDE2IDE1LjA2NzggMTUuMzE1NSAxNC43NzY5IDE0LjczMzdaTTMuMTYwMDcgMTQuMjVMNy44NjkyOSA0LjgzMTU2TDEyLjU3ODUgMTQuMjVIMy4xNjAwN1pNOC43NDQyOSAxMS42MjVWMTMuMzc1SDYuOTk0MjlWMTEuNjI1SDguNzQ0MjlaTTYuOTk0MjkgMTAuNzVWNy4yNUg4Ljc0NDI5VjEwLjc1SDYuOTk0MjlaIiBmaWxsPSIjRUM3MjExIi8+CjxwYXRoIGQ9Ik0xMS4xOTkxIDIuOTUyMzhDMTAuODgwOSAyLjMxNDY3IDEwLjM1MzcgMS44MDUyNiA5LjcwNTUgMS41MDlMMTEuMDQxIDEuMDY5NzhDMTEuNjg4MyAwLjk0OTgxNCAxMi4zMzcgMS4yNzI2MyAxMi42MzE3IDEuODYxNDFMMTcuNjEzNiAxMS44MTYxQzE4LjM1MjcgMTMuMjkyOSAxNy41OTM4IDE1LjA4MDQgMTYuMDE4IDE1LjU3NDVDMTYuNDA0NCAxNC40NTA3IDE2LjMyMzEgMTMuMjE4OCAxNS43OTI0IDEyLjE1NTVMMTEuMTk5MSAyLjk1MjM4WiIgZmlsbD0iI0VDNzIxMSIvPgo8L3N2Zz4=");
    background-color: darkorange;
}

.ace_scrollbar {
    contain: strict;
    position: absolute;
    right: 0;
    bottom: 0;
    z-index: 6;
}

.ace_scrollbar-inner {
    position: absolute;
    cursor: text;
    left: 0;
    top: 0;
}

.ace_scrollbar-v{
    overflow-x: hidden;
    overflow-y: scroll;
    top: 0;
}

.ace_scrollbar-h {
    overflow-x: scroll;
    overflow-y: hidden;
    left: 0;
}

.ace_print-margin {
    position: absolute;
    height: 100%;
}

.ace_text-input {
    position: absolute;
    z-index: 0;
    width: 0.5em;
    height: 1em;
    opacity: 0;
    background: transparent;
    -moz-appearance: none;
    appearance: none;
    border: none;
    resize: none;
    outline: none;
    overflow: hidden;
    font: inherit;
    padding: 0 1px;
    margin: 0 -1px;
    contain: strict;
    -ms-user-select: text;
    -moz-user-select: text;
    -webkit-user-select: text;
    user-select: text;
    /*with `pre-line` chrome inserts &nbsp; instead of space*/
    white-space: pre!important;
}
.ace_text-input.ace_composition {
    background: transparent;
    color: inherit;
    z-index: 1000;
    opacity: 1;
}
.ace_composition_placeholder { color: transparent }
.ace_composition_marker { 
    border-bottom: 1px solid;
    position: absolute;
    border-radius: 0;
    margin-top: 1px;
}

[ace_nocontext=true] {
    transform: none!important;
    filter: none!important;
    clip-path: none!important;
    mask : none!important;
    contain: none!important;
    perspective: none!important;
    mix-blend-mode: initial!important;
    z-index: auto;
}

.ace_layer {
    z-index: 1;
    position: absolute;
    overflow: hidden;
    /* workaround for chrome bug https://github.com/ajaxorg/ace/issues/2312*/
    word-wrap: normal;
    white-space: pre;
    height: 100%;
    width: 100%;
    box-sizing: border-box;
    /* setting pointer-events: auto; on node under the mouse, which changes
        during scroll, will break mouse wheel scrolling in Safari */
    pointer-events: none;
}

.ace_gutter-layer {
    position: relative;
    width: auto;
    text-align: right;
    pointer-events: auto;
    height: 1000000px;
    contain: style size layout;
}

.ace_text-layer {
    font: inherit !important;
    position: absolute;
    height: 1000000px;
    width: 1000000px;
    contain: style size layout;
}

.ace_text-layer > .ace_line, .ace_text-layer > .ace_line_group {
    contain: style size layout;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
}

.ace_hidpi .ace_text-layer,
.ace_hidpi .ace_gutter-layer,
.ace_hidpi .ace_content,
.ace_hidpi .ace_gutter {
    contain: strict;
}
.ace_hidpi .ace_text-layer > .ace_line, 
.ace_hidpi .ace_text-layer > .ace_line_group {
    contain: strict;
}

.ace_cjk {
    display: inline-block;
    text-align: center;
}

.ace_cursor-layer {
    z-index: 4;
}

.ace_cursor {
    z-index: 4;
    position: absolute;
    box-sizing: border-box;
    border-left: 2px solid;
    /* workaround for smooth cursor repaintng whole screen in chrome */
    transform: translatez(0);
}

.ace_multiselect .ace_cursor {
    border-left-width: 1px;
}

.ace_slim-cursors .ace_cursor {
    border-left-width: 1px;
}

.ace_overwrite-cursors .ace_cursor {
    border-left-width: 0;
    border-bottom: 1px solid;
}

.ace_hidden-cursors .ace_cursor {
    opacity: 0.2;
}

.ace_hasPlaceholder .ace_hidden-cursors .ace_cursor {
    opacity: 0;
}

.ace_smooth-blinking .ace_cursor {
    transition: opacity 0.18s;
}

.ace_animate-blinking .ace_cursor {
    animation-duration: 1000ms;
    animation-timing-function: step-end;
    animation-name: blink-ace-animate;
    animation-iteration-count: infinite;
}

.ace_animate-blinking.ace_smooth-blinking .ace_cursor {
    animation-duration: 1000ms;
    animation-timing-function: ease-in-out;
    animation-name: blink-ace-animate-smooth;
}
    
@keyframes blink-ace-animate {
    from, to { opacity: 1; }
    60% { opacity: 0; }
}

@keyframes blink-ace-animate-smooth {
    from, to { opacity: 1; }
    45% { opacity: 1; }
    60% { opacity: 0; }
    85% { opacity: 0; }
}

.ace_marker-layer .ace_step, .ace_marker-layer .ace_stack {
    position: absolute;
    z-index: 3;
}

.ace_marker-layer .ace_selection {
    position: absolute;
    z-index: 5;
}

.ace_marker-layer .ace_bracket {
    position: absolute;
    z-index: 6;
}

.ace_marker-layer .ace_error_bracket {
    position: absolute;
    border-bottom: 1px solid #DE5555;
    border-radius: 0;
}

.ace_marker-layer .ace_active-line {
    position: absolute;
    z-index: 2;
}

.ace_marker-layer .ace_selected-word {
    position: absolute;
    z-index: 4;
    box-sizing: border-box;
}

.ace_line .ace_fold {
    box-sizing: border-box;

    display: inline-block;
    height: 11px;
    margin-top: -2px;
    vertical-align: middle;

    background-image:
        url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAJCAYAAADU6McMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJpJREFUeNpi/P//PwOlgAXGYGRklAVSokD8GmjwY1wasKljQpYACtpCFeADcHVQfQyMQAwzwAZI3wJKvCLkfKBaMSClBlR7BOQikCFGQEErIH0VqkabiGCAqwUadAzZJRxQr/0gwiXIal8zQQPnNVTgJ1TdawL0T5gBIP1MUJNhBv2HKoQHHjqNrA4WO4zY0glyNKLT2KIfIMAAQsdgGiXvgnYAAAAASUVORK5CYII="),
        url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAA3CAYAAADNNiA5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACJJREFUeNpi+P//fxgTAwPDBxDxD078RSX+YeEyDFMCIMAAI3INmXiwf2YAAAAASUVORK5CYII=");
    background-repeat: no-repeat, repeat-x;
    background-position: center center, top left;
    color: transparent;

    border: 1px solid black;
    border-radius: 2px;

    cursor: pointer;
    pointer-events: auto;
}

.ace_dark .ace_fold {
}

.ace_fold:hover{
    background-image:
        url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAJCAYAAADU6McMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJpJREFUeNpi/P//PwOlgAXGYGRklAVSokD8GmjwY1wasKljQpYACtpCFeADcHVQfQyMQAwzwAZI3wJKvCLkfKBaMSClBlR7BOQikCFGQEErIH0VqkabiGCAqwUadAzZJRxQr/0gwiXIal8zQQPnNVTgJ1TdawL0T5gBIP1MUJNhBv2HKoQHHjqNrA4WO4zY0glyNKLT2KIfIMAAQsdgGiXvgnYAAAAASUVORK5CYII="),
        url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAA3CAYAAADNNiA5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACBJREFUeNpi+P//fz4TAwPDZxDxD5X4i5fLMEwJgAADAEPVDbjNw87ZAAAAAElFTkSuQmCC");
}

.ace_tooltip {
    background-color: #f5f5f5;
    border: 1px solid gray;
    border-radius: 1px;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
    color: black;
    max-width: 100%;
    padding: 3px 4px;
    position: fixed;
    z-index: 999999;
    box-sizing: border-box;
    cursor: default;
    white-space: pre-wrap;
    word-wrap: break-word;
    line-height: normal;
    font-style: normal;
    font-weight: normal;
    letter-spacing: normal;
    pointer-events: none;
    overflow: auto;
    max-width: min(60em, 66vw);
    overscroll-behavior: contain;
}
.ace_tooltip pre {
    white-space: pre-wrap;
}

.ace_tooltip.ace_dark {
    background-color: #636363;
    color: #fff;
}

.ace_tooltip:focus {
    outline: 1px solid #5E9ED6;
}

.ace_icon {
    display: inline-block;
    width: 18px;
    vertical-align: top;
}

.ace_icon_svg {
    display: inline-block;
    width: 12px;
    vertical-align: top;
    -webkit-mask-repeat: no-repeat;
    -webkit-mask-size: 12px;
    -webkit-mask-position: center;
}

.ace_folding-enabled > .ace_gutter-cell, .ace_folding-enabled > .ace_gutter-cell_svg-icons {
    padding-right: 13px;
}

.ace_fold-widget {
    box-sizing: border-box;

    margin: 0 -12px 0 1px;
    display: none;
    width: 11px;
    vertical-align: top;

    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAANElEQVR42mWKsQ0AMAzC8ixLlrzQjzmBiEjp0A6WwBCSPgKAXoLkqSot7nN3yMwR7pZ32NzpKkVoDBUxKAAAAABJRU5ErkJggg==");
    background-repeat: no-repeat;
    background-position: center;

    border-radius: 3px;
    
    border: 1px solid transparent;
    cursor: pointer;
}

.ace_folding-enabled .ace_fold-widget {
    display: inline-block;   
}

.ace_fold-widget.ace_end {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAANElEQVR42m3HwQkAMAhD0YzsRchFKI7sAikeWkrxwScEB0nh5e7KTPWimZki4tYfVbX+MNl4pyZXejUO1QAAAABJRU5ErkJggg==");
}

.ace_fold-widget.ace_closed {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAGCAYAAAAG5SQMAAAAOUlEQVR42jXKwQkAMAgDwKwqKD4EwQ26sSOkVWjgIIHAzPiCgaqiqnJHZnKICBERHN194O5b9vbLuAVRL+l0YWnZAAAAAElFTkSuQmCCXA==");
}

.ace_fold-widget:hover {
    border: 1px solid rgba(0, 0, 0, 0.3);
    background-color: rgba(255, 255, 255, 0.2);
    box-shadow: 0 1px 1px rgba(255, 255, 255, 0.7);
}

.ace_fold-widget:active {
    border: 1px solid rgba(0, 0, 0, 0.4);
    background-color: rgba(0, 0, 0, 0.05);
    box-shadow: 0 1px 1px rgba(255, 255, 255, 0.8);
}
/**
 * Dark version for fold widgets
 */
.ace_dark .ace_fold-widget {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHklEQVQIW2P4//8/AzoGEQ7oGCaLLAhWiSwB146BAQCSTPYocqT0AAAAAElFTkSuQmCC");
}
.ace_dark .ace_fold-widget.ace_end {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAH0lEQVQIW2P4//8/AxQ7wNjIAjDMgC4AxjCVKBirIAAF0kz2rlhxpAAAAABJRU5ErkJggg==");
}
.ace_dark .ace_fold-widget.ace_closed {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAFCAYAAACAcVaiAAAAHElEQVQIW2P4//+/AxAzgDADlOOAznHAKgPWAwARji8UIDTfQQAAAABJRU5ErkJggg==");
}
.ace_dark .ace_fold-widget:hover {
    box-shadow: 0 1px 1px rgba(255, 255, 255, 0.2);
    background-color: rgba(255, 255, 255, 0.1);
}
.ace_dark .ace_fold-widget:active {
    box-shadow: 0 1px 1px rgba(255, 255, 255, 0.2);
}

.ace_inline_button {
    border: 1px solid lightgray;
    display: inline-block;
    margin: -1px 8px;
    padding: 0 5px;
    pointer-events: auto;
    cursor: pointer;
}
.ace_inline_button:hover {
    border-color: gray;
    background: rgba(200,200,200,0.2);
    display: inline-block;
    pointer-events: auto;
}

.ace_fold-widget.ace_invalid {
    background-color: #FFB4B4;
    border-color: #DE5555;
}

.ace_fade-fold-widgets .ace_fold-widget {
    transition: opacity 0.4s ease 0.05s;
    opacity: 0;
}

.ace_fade-fold-widgets:hover .ace_fold-widget {
    transition: opacity 0.05s ease 0.05s;
    opacity:1;
}

.ace_underline {
    text-decoration: underline;
}

.ace_bold {
    font-weight: bold;
}

.ace_nobold .ace_bold {
    font-weight: normal;
}

.ace_italic {
    font-style: italic;
}


.ace_error-marker {
    background-color: rgba(255, 0, 0,0.2);
    position: absolute;
    z-index: 9;
}

.ace_highlight-marker {
    background-color: rgba(255, 255, 0,0.2);
    position: absolute;
    z-index: 8;
}

.ace_mobile-menu {
    position: absolute;
    line-height: 1.5;
    border-radius: 4px;
    -ms-user-select: none;
    -moz-user-select: none;
    -webkit-user-select: none;
    user-select: none;
    background: white;
    box-shadow: 1px 3px 2px grey;
    border: 1px solid #dcdcdc;
    color: black;
}
.ace_dark > .ace_mobile-menu {
    background: #333;
    color: #ccc;
    box-shadow: 1px 3px 2px grey;
    border: 1px solid #444;

}
.ace_mobile-button {
    padding: 2px;
    cursor: pointer;
    overflow: hidden;
}
.ace_mobile-button:hover {
    background-color: #eee;
    opacity:1;
}
.ace_mobile-button:active {
    background-color: #ddd;
}

.ace_placeholder {
    font-family: arial;
    transform: scale(0.9);
    transform-origin: left;
    white-space: pre;
    opacity: 0.7;
    margin: 0 10px;
}

.ace_ghost_text {
    opacity: 0.5;
    font-style: italic;
}

.ace_ghost_text > div {
    white-space: pre;
}

.ghost_text_line_wrapped::after {
    content: "↩";
    position: absolute;
}

.ace_lineWidgetContainer.ace_ghost_text {
    margin: 0px 4px
}

.ace_screenreader-only {
    position:absolute;
    left:-10000px;
    top:auto;
    width:1px;
    height:1px;
    overflow:hidden;
}
/*# sourceURL=ace/css/ace_editor.css */</style><style id="ace_scrollbar.css">.ace_editor>.ace_sb-v div, .ace_editor>.ace_sb-h div{
  position: absolute;
  background: rgba(128, 128, 128, 0.6);
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  border: 1px solid #bbb;
  border-radius: 2px;
  z-index: 8;
}
.ace_editor>.ace_sb-v, .ace_editor>.ace_sb-h {
  position: absolute;
  z-index: 6;
  background: none;
  overflow: hidden!important;
}
.ace_editor>.ace_sb-v {
  z-index: 6;
  right: 0;
  top: 0;
  width: 12px;
}
.ace_editor>.ace_sb-v div {
  z-index: 8;
  right: 0;
  width: 100%;
}
.ace_editor>.ace_sb-h {
  bottom: 0;
  left: 0;
  height: 12px;
}
.ace_editor>.ace_sb-h div {
  bottom: 0;
  height: 100%;
}
.ace_editor>.ace_sb_grabbed {
  z-index: 8;
  background: #000;
}
/*# sourceURL=ace/css/ace_scrollbar.css */</style>
  <link rel="icon" href="https://www.codechef.com/favicon.ico" type="image/x-icon">
  <title>Cricket World Cup Qualifier Practice Problem in 500 difficulty rating</title>
  
  <meta name="description" content="Test your  knowledge with our Cricket World Cup Qualifier practice problem.  Dive into the world of basic-programming-concepts challenges at CodeChef.">
  <meta name="og:image" content="https://cdn.codechef.com/sites/all/themes/abessive/cc-logo.png">
  <meta name="og:type" content="website">
  <meta name="theme-color" content="#000000">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CWC23QUALIF">
  <script type="text/javascript" async="" src="./cric12_files/analytics.js.download"></script><script type="text/javascript" async="" src="./cric12_files/js"></script><script async="" src="./cric12_files/gtm.js.download"></script><script async="" src="./cric12_files/client" type="text/javascript"></script>

  <script type="text/javascript">

    const languageIdeRoutes = [
      'python', 'java', 'cpp', 'c', 'pypy', 'csharp', 'javascript', 'go', 'php', 'kotlin', 'rust', 'r', 'sql', 'html',
      'oracledb'
    ];

    if (
      (['pro', 'contests'].includes(window.location.pathname.split('/').filter(Boolean).pop())) ||
      (['learn', 'games', 'viewsolution',
        'submit', 'practice', 'dashboard', 'getting-started', 'skill-test', 'college-program', 'practice-old',
        'roadmap', 'blogs', 'roadmaps', 'blogs', 'skill-tests', 'ide', 'mobile'
      ].includes(window.location.pathname.split('/').filter(Boolean)[0])) ||
      (['submit'].includes(window.location.pathname.split('/').filter(Boolean)[1])) ||
      (['status'].includes(window.location.pathname.split('/').filter(Boolean).slice(-2, -1).pop())) || [
        // Regex to match the practice and contest submit routes
        /^\/(submit\/([A-Z]+[A-Z0-9_]*)+|problems\/([A-Z]+[A-Z0-9_]*)+|([A-Z]+[A-Z0-9_]*)+\/submit\/([A-Z]+[A-Z0-9_]*)+|([A-Z]+[A-Z0-9_]*)+\/problems\/([A-Z]+[A-Z0-9_]*)+)$/
      ].some((regexp) => (regexp.test(window.location.pathname))) ||
      (languageIdeRoutes.some(lang => window.location.pathname.includes(`${lang}-online-compiler`)))
    ) {
      const metaElement = document.createElement('meta');
      metaElement.setAttribute('name', 'viewport');
      metaElement.setAttribute('content', 'width=device-width, initial-scale=1');
      document.head.appendChild(metaElement);
    }

    (function (w, d, s, l, i) {
      w[l] = w[l] || [];
      w[l].push({
        'gtm.start': new Date().getTime(),
        event: 'gtm.js'
      });
      var f = d.getElementsByTagName(s)[0],
        j = d.createElement(s),
        dl = l != 'dataLayer' ? '&l=' + l : '';
      j.async = true;
      j.src =
        'https://www.googletagmanager.com/gtm.js?id=' + i + dl;
      f.parentNode.insertBefore(j, f);
    })(window, document, 'script', 'dataLayer', 'GTM-TV5X2M');
  </script>
  <script type="module" crossorigin="" src="./cric12_files/index-9f4W_Kkj.js.download"></script>
  <link rel="modulepreload" crossorigin="" href="https://static.codechef.com/build/react2/assets/moment-HmOkGw2I.js">
  <link rel="modulepreload" crossorigin="" href="https://static.codechef.com/build/react2/assets/vendor-qZKDd1yc.js">
  <link rel="modulepreload" crossorigin="" href="https://static.codechef.com/build/react2/assets/@material-ui-cxq1kyWC.js">
  <link rel="modulepreload" crossorigin="" href="https://static.codechef.com/build/react2/assets/sweetalert2-7m5fHpSs.js">
  <link rel="modulepreload" crossorigin="" href="https://static.codechef.com/build/react2/assets/react-router-dom-WRqnmta6.js">
  <link rel="stylesheet" crossorigin="" href="./cric12_files/sweetalert2-xhNZC6U0.css">
  <link rel="stylesheet" crossorigin="" href="./cric12_files/index-jz53_3Ep.css">
<meta name="viewport" content="width=device-width, initial-scale=1"><style id="googleidentityservice_button_styles">.qJTHM{-webkit-user-select:none;color:#202124;direction:ltr;-webkit-touch-callout:none;font-family:"Roboto-Regular",arial,sans-serif;-webkit-font-smoothing:antialiased;font-weight:400;margin:0;overflow:hidden;-webkit-text-size-adjust:100%}.ynRLnc{left:-9999px;position:absolute;top:-9999px}.L6cTce{display:none}.bltWBb{word-break:break-all}.hSRGPd{color:#1a73e8;cursor:pointer;font-weight:500;text-decoration:none}.Bz112c-W3lGp{height:16px;width:16px}.Bz112c-E3DyYd{height:20px;width:20px}.Bz112c-r9oPif{height:24px;width:24px}.Bz112c-uaxL4e{-webkit-border-radius:10px;border-radius:10px}.LgbsSe-Bz112c{display:block}.S9gUrf-YoZ4jf,.S9gUrf-YoZ4jf *{border:none;margin:0;padding:0}.fFW7wc-ibnC6b>.aZ2wEe>div{border-color:#4285f4}.P1ekSe-ZMv3u>div:nth-child(1){background-color:#1a73e8!important}.P1ekSe-ZMv3u>div:nth-child(2),.P1ekSe-ZMv3u>div:nth-child(3){background-image:linear-gradient(to right,rgba(255,255,255,.7),rgba(255,255,255,.7)),linear-gradient(to right,#1a73e8,#1a73e8)!important}.haAclf{display:inline-block}.nsm7Bb-HzV7m-LgbsSe{-webkit-border-radius:4px;border-radius:4px;-webkit-box-sizing:border-box;box-sizing:border-box;-webkit-transition:background-color .218s,border-color .218s;transition:background-color .218s,border-color .218s;-webkit-user-select:none;-webkit-appearance:none;background-color:#fff;background-image:none;border:1px solid #dadce0;color:#3c4043;cursor:pointer;font-family:"Google Sans",arial,sans-serif;font-size:14px;height:40px;letter-spacing:0.25px;outline:none;overflow:hidden;padding:0 12px;position:relative;text-align:center;vertical-align:middle;white-space:nowrap;width:auto}@media screen and (-ms-high-contrast:active){.nsm7Bb-HzV7m-LgbsSe{border:2px solid windowText;color:windowText}}.nsm7Bb-HzV7m-LgbsSe.pSzOP-SxQuSe{font-size:14px;height:32px;letter-spacing:0.25px;padding:0 10px}.nsm7Bb-HzV7m-LgbsSe.purZT-SxQuSe{font-size:11px;height:20px;letter-spacing:0.3px;padding:0 8px}.nsm7Bb-HzV7m-LgbsSe.Bz112c-LgbsSe{padding:0;width:40px}.nsm7Bb-HzV7m-LgbsSe.Bz112c-LgbsSe.pSzOP-SxQuSe{width:32px}.nsm7Bb-HzV7m-LgbsSe.Bz112c-LgbsSe.purZT-SxQuSe{width:20px}.nsm7Bb-HzV7m-LgbsSe.JGcpL-RbRzK{-webkit-border-radius:20px;border-radius:20px}.nsm7Bb-HzV7m-LgbsSe.JGcpL-RbRzK.pSzOP-SxQuSe{-webkit-border-radius:16px;border-radius:16px}.nsm7Bb-HzV7m-LgbsSe.JGcpL-RbRzK.purZT-SxQuSe{-webkit-border-radius:10px;border-radius:10px}.nsm7Bb-HzV7m-LgbsSe.MFS4be-Ia7Qfc{border:none;color:#fff}.nsm7Bb-HzV7m-LgbsSe.MFS4be-v3pZbf-Ia7Qfc{background-color:#1a73e8}.nsm7Bb-HzV7m-LgbsSe.MFS4be-JaPV2b-Ia7Qfc{background-color:#202124;color:#e8eaed}.nsm7Bb-HzV7m-LgbsSe .nsm7Bb-HzV7m-LgbsSe-Bz112c{height:18px;margin-right:8px;min-width:18px;width:18px}.nsm7Bb-HzV7m-LgbsSe.pSzOP-SxQuSe .nsm7Bb-HzV7m-LgbsSe-Bz112c{height:14px;min-width:14px;width:14px}.nsm7Bb-HzV7m-LgbsSe.purZT-SxQuSe .nsm7Bb-HzV7m-LgbsSe-Bz112c{height:10px;min-width:10px;width:10px}.nsm7Bb-HzV7m-LgbsSe.jVeSEe .nsm7Bb-HzV7m-LgbsSe-Bz112c{margin-left:8px;margin-right:-4px}.nsm7Bb-HzV7m-LgbsSe.Bz112c-LgbsSe .nsm7Bb-HzV7m-LgbsSe-Bz112c{margin:0;padding:10px}.nsm7Bb-HzV7m-LgbsSe.Bz112c-LgbsSe.pSzOP-SxQuSe .nsm7Bb-HzV7m-LgbsSe-Bz112c{padding:8px}.nsm7Bb-HzV7m-LgbsSe.Bz112c-LgbsSe.purZT-SxQuSe .nsm7Bb-HzV7m-LgbsSe-Bz112c{padding:4px}.nsm7Bb-HzV7m-LgbsSe .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf{-webkit-border-top-left-radius:3px;border-top-left-radius:3px;-webkit-border-bottom-left-radius:3px;border-bottom-left-radius:3px;display:-webkit-box;display:-webkit-flex;display:flex;justify-content:center;-webkit-align-items:center;align-items:center;background-color:#fff;height:36px;margin-left:-10px;margin-right:12px;min-width:36px;width:36px}.nsm7Bb-HzV7m-LgbsSe .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf .nsm7Bb-HzV7m-LgbsSe-Bz112c,.nsm7Bb-HzV7m-LgbsSe.Bz112c-LgbsSe .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf .nsm7Bb-HzV7m-LgbsSe-Bz112c{margin:0;padding:0}.nsm7Bb-HzV7m-LgbsSe.pSzOP-SxQuSe .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf{height:28px;margin-left:-8px;margin-right:10px;min-width:28px;width:28px}.nsm7Bb-HzV7m-LgbsSe.purZT-SxQuSe .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf{height:16px;margin-left:-6px;margin-right:8px;min-width:16px;width:16px}.nsm7Bb-HzV7m-LgbsSe.Bz112c-LgbsSe .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf{-webkit-border-radius:3px;border-radius:3px;margin-left:2px;margin-right:0;padding:0}.nsm7Bb-HzV7m-LgbsSe.JGcpL-RbRzK .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf{-webkit-border-radius:18px;border-radius:18px}.nsm7Bb-HzV7m-LgbsSe.pSzOP-SxQuSe.JGcpL-RbRzK .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf{-webkit-border-radius:14px;border-radius:14px}.nsm7Bb-HzV7m-LgbsSe.purZT-SxQuSe.JGcpL-RbRzK .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf{-webkit-border-radius:8px;border-radius:8px}.nsm7Bb-HzV7m-LgbsSe .nsm7Bb-HzV7m-LgbsSe-bN97Pc-sM5MNb{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-align-items:center;align-items:center;-webkit-flex-direction:row;flex-direction:row;justify-content:space-between;-webkit-flex-wrap:nowrap;flex-wrap:nowrap;height:100%;position:relative;width:100%}.nsm7Bb-HzV7m-LgbsSe .oXtfBe-l4eHX{justify-content:center}.nsm7Bb-HzV7m-LgbsSe .nsm7Bb-HzV7m-LgbsSe-BPrWId{-webkit-flex-grow:1;flex-grow:1;font-family:"Google Sans",arial,sans-serif;font-weight:500;overflow:hidden;text-overflow:ellipsis;vertical-align:top}.nsm7Bb-HzV7m-LgbsSe.purZT-SxQuSe .nsm7Bb-HzV7m-LgbsSe-BPrWId{font-weight:300}.nsm7Bb-HzV7m-LgbsSe .oXtfBe-l4eHX .nsm7Bb-HzV7m-LgbsSe-BPrWId{-webkit-flex-grow:0;flex-grow:0}.nsm7Bb-HzV7m-LgbsSe .nsm7Bb-HzV7m-LgbsSe-MJoBVe{-webkit-transition:background-color .218s;transition:background-color .218s;bottom:0;left:0;position:absolute;right:0;top:0}.nsm7Bb-HzV7m-LgbsSe:hover,.nsm7Bb-HzV7m-LgbsSe:focus{-webkit-box-shadow:none;box-shadow:none;border-color:#d2e3fc;outline:none}.nsm7Bb-HzV7m-LgbsSe:hover .nsm7Bb-HzV7m-LgbsSe-MJoBVe,.nsm7Bb-HzV7m-LgbsSe:focus .nsm7Bb-HzV7m-LgbsSe-MJoBVe{background:rgba(66,133,244,.04)}.nsm7Bb-HzV7m-LgbsSe:active .nsm7Bb-HzV7m-LgbsSe-MJoBVe{background:rgba(66,133,244,.1)}.nsm7Bb-HzV7m-LgbsSe.MFS4be-Ia7Qfc:hover .nsm7Bb-HzV7m-LgbsSe-MJoBVe,.nsm7Bb-HzV7m-LgbsSe.MFS4be-Ia7Qfc:focus .nsm7Bb-HzV7m-LgbsSe-MJoBVe{background:rgba(255,255,255,.24)}.nsm7Bb-HzV7m-LgbsSe.MFS4be-Ia7Qfc:active .nsm7Bb-HzV7m-LgbsSe-MJoBVe{background:rgba(255,255,255,.32)}.nsm7Bb-HzV7m-LgbsSe .n1UuX-DkfjY{-webkit-border-radius:50%;border-radius:50%;display:-webkit-box;display:-webkit-flex;display:flex;height:20px;margin-left:-4px;margin-right:8px;min-width:20px;width:20px}.nsm7Bb-HzV7m-LgbsSe.jVeSEe .nsm7Bb-HzV7m-LgbsSe-BPrWId{font-family:"Roboto";font-size:12px;text-align:left}.nsm7Bb-HzV7m-LgbsSe.jVeSEe .nsm7Bb-HzV7m-LgbsSe-BPrWId .ssJRIf,.nsm7Bb-HzV7m-LgbsSe.jVeSEe .nsm7Bb-HzV7m-LgbsSe-BPrWId .K4efff .fmcmS{overflow:hidden;text-overflow:ellipsis}.nsm7Bb-HzV7m-LgbsSe.jVeSEe .nsm7Bb-HzV7m-LgbsSe-BPrWId .K4efff{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-align-items:center;align-items:center;color:#5f6368;fill:#5f6368;font-size:11px;font-weight:400}.nsm7Bb-HzV7m-LgbsSe.jVeSEe.MFS4be-Ia7Qfc .nsm7Bb-HzV7m-LgbsSe-BPrWId .K4efff{color:#e8eaed;fill:#e8eaed}.nsm7Bb-HzV7m-LgbsSe.jVeSEe .nsm7Bb-HzV7m-LgbsSe-BPrWId .K4efff .Bz112c{height:18px;margin:-3px -3px -3px 2px;min-width:18px;width:18px}.nsm7Bb-HzV7m-LgbsSe.jVeSEe .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf{-webkit-border-top-left-radius:0;border-top-left-radius:0;-webkit-border-bottom-left-radius:0;border-bottom-left-radius:0;-webkit-border-top-right-radius:3px;border-top-right-radius:3px;-webkit-border-bottom-right-radius:3px;border-bottom-right-radius:3px;margin-left:12px;margin-right:-10px}.nsm7Bb-HzV7m-LgbsSe.jVeSEe.JGcpL-RbRzK .nsm7Bb-HzV7m-LgbsSe-Bz112c-haAclf{-webkit-border-radius:18px;border-radius:18px}.L5Fo6c-sM5MNb{border:0;display:block;left:0;position:relative;top:0}.L5Fo6c-bF1uUb{-webkit-border-radius:4px;border-radius:4px;bottom:0;cursor:pointer;left:0;position:absolute;right:0;top:0}.L5Fo6c-bF1uUb:focus{border:none;outline:none}sentinel{}</style><script type="text/javascript" async="" src="./cric12_files/f.txt"></script><style data-jss="" data-meta="MuiSvgIcon">
.MuiSvgIcon-root {
  fill: currentColor;
  width: 1em;
  height: 1em;
  display: inline-block;
  font-size: 1.5rem;
  transition: fill 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
  flex-shrink: 0;
  user-select: none;
}
.MuiSvgIcon-colorPrimary {
  color: #3f51b5;
}
.MuiSvgIcon-colorSecondary {
  color: #f50057;
}
.MuiSvgIcon-colorAction {
  color: rgba(0, 0, 0, 0.54);
}
.MuiSvgIcon-colorError {
  color: #f44336;
}
.MuiSvgIcon-colorDisabled {
  color: rgba(0, 0, 0, 0.26);
}
.MuiSvgIcon-fontSizeInherit {
  font-size: inherit;
}
.MuiSvgIcon-fontSizeSmall {
  font-size: 1.25rem;
}
.MuiSvgIcon-fontSizeLarge {
  font-size: 2.1875rem;
}
</style><style data-jss="" data-meta="MuiCollapse">
.MuiCollapse-container {
  height: 0;
  overflow: hidden;
  transition: height 300ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
}
.MuiCollapse-entered {
  height: auto;
  overflow: visible;
}
.MuiCollapse-hidden {
  visibility: hidden;
}
.MuiCollapse-wrapper {
  display: flex;
}
.MuiCollapse-wrapperInner {
  width: 100%;
}
</style><style data-jss="" data-meta="MuiPaper">
.MuiPaper-root {
  color: rgba(0, 0, 0, 0.87);
  transition: box-shadow 300ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
  background-color: #fff;
}
.MuiPaper-rounded {
  border-radius: 4px;
}
.MuiPaper-outlined {
  border: 1px solid rgba(0, 0, 0, 0.12);
}
.MuiPaper-elevation0 {
  box-shadow: none;
}
.MuiPaper-elevation1 {
  box-shadow: 0px 2px 1px -1px rgba(0,0,0,0.2),0px 1px 1px 0px rgba(0,0,0,0.14),0px 1px 3px 0px rgba(0,0,0,0.12);
}
.MuiPaper-elevation2 {
  box-shadow: 0px 3px 1px -2px rgba(0,0,0,0.2),0px 2px 2px 0px rgba(0,0,0,0.14),0px 1px 5px 0px rgba(0,0,0,0.12);
}
.MuiPaper-elevation3 {
  box-shadow: 0px 3px 3px -2px rgba(0,0,0,0.2),0px 3px 4px 0px rgba(0,0,0,0.14),0px 1px 8px 0px rgba(0,0,0,0.12);
}
.MuiPaper-elevation4 {
  box-shadow: 0px 2px 4px -1px rgba(0,0,0,0.2),0px 4px 5px 0px rgba(0,0,0,0.14),0px 1px 10px 0px rgba(0,0,0,0.12);
}
.MuiPaper-elevation5 {
  box-shadow: 0px 3px 5px -1px rgba(0,0,0,0.2),0px 5px 8px 0px rgba(0,0,0,0.14),0px 1px 14px 0px rgba(0,0,0,0.12);
}
.MuiPaper-elevation6 {
  box-shadow: 0px 3px 5px -1px rgba(0,0,0,0.2),0px 6px 10px 0px rgba(0,0,0,0.14),0px 1px 18px 0px rgba(0,0,0,0.12);
}
.MuiPaper-elevation7 {
  box-shadow: 0px 4px 5px -2px rgba(0,0,0,0.2),0px 7px 10px 1px rgba(0,0,0,0.14),0px 2px 16px 1px rgba(0,0,0,0.12);
}
.MuiPaper-elevation8 {
  box-shadow: 0px 5px 5px -3px rgba(0,0,0,0.2),0px 8px 10px 1px rgba(0,0,0,0.14),0px 3px 14px 2px rgba(0,0,0,0.12);
}
.MuiPaper-elevation9 {
  box-shadow: 0px 5px 6px -3px rgba(0,0,0,0.2),0px 9px 12px 1px rgba(0,0,0,0.14),0px 3px 16px 2px rgba(0,0,0,0.12);
}
.MuiPaper-elevation10 {
  box-shadow: 0px 6px 6px -3px rgba(0,0,0,0.2),0px 10px 14px 1px rgba(0,0,0,0.14),0px 4px 18px 3px rgba(0,0,0,0.12);
}
.MuiPaper-elevation11 {
  box-shadow: 0px 6px 7px -4px rgba(0,0,0,0.2),0px 11px 15px 1px rgba(0,0,0,0.14),0px 4px 20px 3px rgba(0,0,0,0.12);
}
.MuiPaper-elevation12 {
  box-shadow: 0px 7px 8px -4px rgba(0,0,0,0.2),0px 12px 17px 2px rgba(0,0,0,0.14),0px 5px 22px 4px rgba(0,0,0,0.12);
}
.MuiPaper-elevation13 {
  box-shadow: 0px 7px 8px -4px rgba(0,0,0,0.2),0px 13px 19px 2px rgba(0,0,0,0.14),0px 5px 24px 4px rgba(0,0,0,0.12);
}
.MuiPaper-elevation14 {
  box-shadow: 0px 7px 9px -4px rgba(0,0,0,0.2),0px 14px 21px 2px rgba(0,0,0,0.14),0px 5px 26px 4px rgba(0,0,0,0.12);
}
.MuiPaper-elevation15 {
  box-shadow: 0px 8px 9px -5px rgba(0,0,0,0.2),0px 15px 22px 2px rgba(0,0,0,0.14),0px 6px 28px 5px rgba(0,0,0,0.12);
}
.MuiPaper-elevation16 {
  box-shadow: 0px 8px 10px -5px rgba(0,0,0,0.2),0px 16px 24px 2px rgba(0,0,0,0.14),0px 6px 30px 5px rgba(0,0,0,0.12);
}
.MuiPaper-elevation17 {
  box-shadow: 0px 8px 11px -5px rgba(0,0,0,0.2),0px 17px 26px 2px rgba(0,0,0,0.14),0px 6px 32px 5px rgba(0,0,0,0.12);
}
.MuiPaper-elevation18 {
  box-shadow: 0px 9px 11px -5px rgba(0,0,0,0.2),0px 18px 28px 2px rgba(0,0,0,0.14),0px 7px 34px 6px rgba(0,0,0,0.12);
}
.MuiPaper-elevation19 {
  box-shadow: 0px 9px 12px -6px rgba(0,0,0,0.2),0px 19px 29px 2px rgba(0,0,0,0.14),0px 7px 36px 6px rgba(0,0,0,0.12);
}
.MuiPaper-elevation20 {
  box-shadow: 0px 10px 13px -6px rgba(0,0,0,0.2),0px 20px 31px 3px rgba(0,0,0,0.14),0px 8px 38px 7px rgba(0,0,0,0.12);
}
.MuiPaper-elevation21 {
  box-shadow: 0px 10px 13px -6px rgba(0,0,0,0.2),0px 21px 33px 3px rgba(0,0,0,0.14),0px 8px 40px 7px rgba(0,0,0,0.12);
}
.MuiPaper-elevation22 {
  box-shadow: 0px 10px 14px -6px rgba(0,0,0,0.2),0px 22px 35px 3px rgba(0,0,0,0.14),0px 8px 42px 7px rgba(0,0,0,0.12);
}
.MuiPaper-elevation23 {
  box-shadow: 0px 11px 14px -7px rgba(0,0,0,0.2),0px 23px 36px 3px rgba(0,0,0,0.14),0px 9px 44px 8px rgba(0,0,0,0.12);
}
.MuiPaper-elevation24 {
  box-shadow: 0px 11px 15px -7px rgba(0,0,0,0.2),0px 24px 38px 3px rgba(0,0,0,0.14),0px 9px 46px 8px rgba(0,0,0,0.12);
}
</style><style data-jss="" data-meta="MuiAccordion">
.MuiAccordion-root {
  position: relative;
  transition: margin 150ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
}
.MuiAccordion-root:before {
  top: -1px;
  left: 0;
  right: 0;
  height: 1px;
  content: "";
  opacity: 1;
  position: absolute;
  transition: opacity 150ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,background-color 150ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
  background-color: rgba(0, 0, 0, 0.12);
}
.MuiAccordion-root.Mui-expanded {
  margin: 16px 0;
}
.MuiAccordion-root.Mui-disabled {
  background-color: rgba(0, 0, 0, 0.12);
}
.MuiAccordion-root.Mui-expanded + .MuiAccordion-root:before {
  display: none;
}
.MuiAccordion-root.Mui-expanded:first-child {
  margin-top: 0;
}
.MuiAccordion-root.Mui-expanded:last-child {
  margin-bottom: 0;
}
.MuiAccordion-root.Mui-expanded:before {
  opacity: 0;
}
.MuiAccordion-root:first-child:before {
  display: none;
}
.MuiAccordion-rounded {
  border-radius: 0;
}
.MuiAccordion-rounded:first-child {
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
}
.MuiAccordion-rounded:last-child {
  border-bottom-left-radius: 4px;
  border-bottom-right-radius: 4px;
}
@supports (-ms-ime-align: auto) {
  .MuiAccordion-rounded:last-child {
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
  }
}
</style><style data-jss="" data-meta="MuiAccordionDetails">
.MuiAccordionDetails-root {
  display: flex;
  padding: 8px 16px 16px;
}
</style><style data-jss="" data-meta="MuiTouchRipple">
.MuiTouchRipple-root {
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 0;
  overflow: hidden;
  position: absolute;
  border-radius: inherit;
  pointer-events: none;
}
.MuiTouchRipple-ripple {
  opacity: 0;
  position: absolute;
}
.MuiTouchRipple-rippleVisible {
  opacity: 0.3;
  animation: MuiTouchRipple-keyframes-enter 550ms cubic-bezier(0.4, 0, 0.2, 1);
  transform: scale(1);
}
.MuiTouchRipple-ripplePulsate {
  animation-duration: 200ms;
}
.MuiTouchRipple-child {
  width: 100%;
  height: 100%;
  display: block;
  opacity: 1;
  border-radius: 50%;
  background-color: currentColor;
}
.MuiTouchRipple-childLeaving {
  opacity: 0;
  animation: MuiTouchRipple-keyframes-exit 550ms cubic-bezier(0.4, 0, 0.2, 1);
}
.MuiTouchRipple-childPulsate {
  top: 0;
  left: 0;
  position: absolute;
  animation: MuiTouchRipple-keyframes-pulsate 2500ms cubic-bezier(0.4, 0, 0.2, 1) 200ms infinite;
}
@-webkit-keyframes MuiTouchRipple-keyframes-enter {
  0% {
    opacity: 0.1;
    transform: scale(0);
  }
  100% {
    opacity: 0.3;
    transform: scale(1);
  }
}
@-webkit-keyframes MuiTouchRipple-keyframes-exit {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}
@-webkit-keyframes MuiTouchRipple-keyframes-pulsate {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(0.92);
  }
  100% {
    transform: scale(1);
  }
}
</style><style data-jss="" data-meta="MuiButtonBase">
.MuiButtonBase-root {
  color: inherit;
  border: 0;
  cursor: pointer;
  margin: 0;
  display: inline-flex;
  outline: 0;
  padding: 0;
  position: relative;
  align-items: center;
  user-select: none;
  border-radius: 0;
  vertical-align: middle;
  -moz-appearance: none;
  justify-content: center;
  text-decoration: none;
  background-color: transparent;
  -webkit-appearance: none;
  -webkit-tap-highlight-color: transparent;
}
.MuiButtonBase-root::-moz-focus-inner {
  border-style: none;
}
.MuiButtonBase-root.Mui-disabled {
  cursor: default;
  pointer-events: none;
}
@media print {
  .MuiButtonBase-root {
    -webkit-print-color-adjust: exact;
  }
}
</style><style data-jss="" data-meta="MuiIconButton">
.MuiIconButton-root {
  flex: 0 0 auto;
  color: rgba(0, 0, 0, 0.54);
  padding: 12px;
  overflow: visible;
  font-size: 1.5rem;
  text-align: center;
  transition: background-color 150ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
  border-radius: 50%;
}
.MuiIconButton-root:hover {
  background-color: rgba(0, 0, 0, 0.04);
}
.MuiIconButton-root.Mui-disabled {
  color: rgba(0, 0, 0, 0.26);
  background-color: transparent;
}
@media (hover: none) {
  .MuiIconButton-root:hover {
    background-color: transparent;
  }
}
.MuiIconButton-edgeStart {
  margin-left: -12px;
}
.MuiIconButton-sizeSmall.MuiIconButton-edgeStart {
  margin-left: -3px;
}
.MuiIconButton-edgeEnd {
  margin-right: -12px;
}
.MuiIconButton-sizeSmall.MuiIconButton-edgeEnd {
  margin-right: -3px;
}
.MuiIconButton-colorInherit {
  color: inherit;
}
.MuiIconButton-colorPrimary {
  color: #3f51b5;
}
.MuiIconButton-colorPrimary:hover {
  background-color: rgba(63, 81, 181, 0.04);
}
@media (hover: none) {
  .MuiIconButton-colorPrimary:hover {
    background-color: transparent;
  }
}
.MuiIconButton-colorSecondary {
  color: #f50057;
}
.MuiIconButton-colorSecondary:hover {
  background-color: rgba(245, 0, 87, 0.04);
}
@media (hover: none) {
  .MuiIconButton-colorSecondary:hover {
    background-color: transparent;
  }
}
.MuiIconButton-sizeSmall {
  padding: 3px;
  font-size: 1.125rem;
}
.MuiIconButton-label {
  width: 100%;
  display: flex;
  align-items: inherit;
  justify-content: inherit;
}
</style><style data-jss="" data-meta="MuiAccordionSummary">
.MuiAccordionSummary-root {
  display: flex;
  padding: 0px 16px;
  min-height: 48px;
  transition: min-height 150ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,background-color 150ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
}
.MuiAccordionSummary-root:hover:not(.Mui-disabled) {
  cursor: pointer;
}
.MuiAccordionSummary-root.Mui-expanded {
  min-height: 64px;
}
.MuiAccordionSummary-root.Mui-focused {
  background-color: rgba(0, 0, 0, 0.12);
}
.MuiAccordionSummary-root.Mui-disabled {
  opacity: 0.38;
}
.MuiAccordionSummary-content {
  margin: 12px 0;
  display: flex;
  flex-grow: 1;
  transition: margin 150ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
}
.MuiAccordionSummary-content.Mui-expanded {
  margin: 20px 0;
}
.MuiAccordionSummary-expandIcon {
  transform: rotate(0deg);
  transition: transform 150ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
}
.MuiAccordionSummary-expandIcon:hover {
  background-color: transparent;
}
.MuiAccordionSummary-expandIcon.Mui-expanded {
  transform: rotate(180deg);
}
</style><style data-jss="" data-meta="MuiBackdrop">
.MuiBackdrop-root {
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  z-index: -1;
  position: fixed;
  align-items: center;
  justify-content: center;
  background-color: rgba(0, 0, 0, 0.5);
  -webkit-tap-highlight-color: transparent;
}
.MuiBackdrop-invisible {
  background-color: transparent;
}
</style><style data-jss="" data-meta="MuiBackdrop">
.MuiBackdrop-root {
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  z-index: -1;
  position: fixed;
  align-items: center;
  justify-content: center;
  background-color: rgba(0, 0, 0, 0.5);
  -webkit-tap-highlight-color: transparent;
}
.MuiBackdrop-invisible {
  background-color: transparent;
}
</style><style data-jss="" data-meta="MuiBox">

</style><style data-jss="" data-meta="MuiBox">
</style><style data-jss="" data-meta="MuiBox">
</style><style data-jss="" data-meta="MuiDialog">
@media print {
  .MuiDialog-root {
    position: absolute !important;
  }
}
.MuiDialog-scrollPaper {
  display: flex;
  align-items: center;
  justify-content: center;
}
.MuiDialog-scrollBody {
  overflow-x: hidden;
  overflow-y: auto;
  text-align: center;
}
.MuiDialog-scrollBody:after {
  width: 0;
  height: 100%;
  content: "";
  display: inline-block;
  vertical-align: middle;
}
.MuiDialog-container {
  height: 100%;
  outline: 0;
}
@media print {
  .MuiDialog-container {
    height: auto;
  }
}
.MuiDialog-paper {
  margin: 32px;
  position: relative;
  overflow-y: auto;
}
@media print {
  .MuiDialog-paper {
    box-shadow: none;
    overflow-y: visible;
  }
}
.MuiDialog-paperScrollPaper {
  display: flex;
  max-height: calc(100% - 64px);
  flex-direction: column;
}
.MuiDialog-paperScrollBody {
  display: inline-block;
  text-align: left;
  vertical-align: middle;
}
.MuiDialog-paperWidthFalse {
  max-width: calc(100% - 64px);
}
.MuiDialog-paperWidthXs {
  max-width: 444px;
}
@media (max-width:507.95px) {
  .MuiDialog-paperWidthXs.MuiDialog-paperScrollBody {
    max-width: calc(100% - 64px);
  }
}
.MuiDialog-paperWidthSm {
  max-width: 600px;
}
@media (max-width:663.95px) {
  .MuiDialog-paperWidthSm.MuiDialog-paperScrollBody {
    max-width: calc(100% - 64px);
  }
}
.MuiDialog-paperWidthMd {
  max-width: 960px;
}
@media (max-width:1023.95px) {
  .MuiDialog-paperWidthMd.MuiDialog-paperScrollBody {
    max-width: calc(100% - 64px);
  }
}
.MuiDialog-paperWidthLg {
  max-width: 1280px;
}
@media (max-width:1343.95px) {
  .MuiDialog-paperWidthLg.MuiDialog-paperScrollBody {
    max-width: calc(100% - 64px);
  }
}
.MuiDialog-paperWidthXl {
  max-width: 1920px;
}
@media (max-width:1983.95px) {
  .MuiDialog-paperWidthXl.MuiDialog-paperScrollBody {
    max-width: calc(100% - 64px);
  }
}
.MuiDialog-paperFullWidth {
  width: calc(100% - 64px);
}
.MuiDialog-paperFullScreen {
  width: 100%;
  height: 100%;
  margin: 0;
  max-width: 100%;
  max-height: none;
  border-radius: 0;
}
.MuiDialog-paperFullScreen.MuiDialog-paperScrollBody {
  margin: 0;
  max-width: 100%;
}
</style><style data-jss="" data-meta="MuiDivider">
.MuiDivider-root {
  border: none;
  height: 1px;
  margin: 0;
  flex-shrink: 0;
  background-color: rgba(0, 0, 0, 0.12);
}
.MuiDivider-absolute {
  left: 0;
  width: 100%;
  bottom: 0;
  position: absolute;
}
.MuiDivider-inset {
  margin-left: 72px;
}
.MuiDivider-light {
  background-color: rgba(0, 0, 0, 0.08);
}
.MuiDivider-middle {
  margin-left: 16px;
  margin-right: 16px;
}
.MuiDivider-vertical {
  width: 1px;
  height: 100%;
}
.MuiDivider-flexItem {
  height: auto;
  align-self: stretch;
}
</style><style data-jss="" data-meta="MuiInputBase">
@-webkit-keyframes mui-auto-fill {}
@-webkit-keyframes mui-auto-fill-cancel {}
.MuiInputBase-root {
  color: rgba(0, 0, 0, 0.87);
  cursor: text;
  display: inline-flex;
  position: relative;
  font-size: 1rem;
  box-sizing: border-box;
  align-items: center;
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 400;
  line-height: 1.1876em;
  letter-spacing: 0.00938em;
}
.MuiInputBase-root.Mui-disabled {
  color: rgba(0, 0, 0, 0.38);
  cursor: default;
}
.MuiInputBase-multiline {
  padding: 6px 0 7px;
}
.MuiInputBase-multiline.MuiInputBase-marginDense {
  padding-top: 3px;
}
.MuiInputBase-fullWidth {
  width: 100%;
}
.MuiInputBase-input {
  font: inherit;
  color: currentColor;
  width: 100%;
  border: 0;
  height: 1.1876em;
  margin: 0;
  display: block;
  padding: 6px 0 7px;
  min-width: 0;
  background: none;
  box-sizing: content-box;
  animation-name: mui-auto-fill-cancel;
  letter-spacing: inherit;
  animation-duration: 10ms;
  -webkit-tap-highlight-color: transparent;
}
.MuiInputBase-input::-webkit-input-placeholder {
  color: currentColor;
  opacity: 0.42;
  transition: opacity 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
}
.MuiInputBase-input::-moz-placeholder {
  color: currentColor;
  opacity: 0.42;
  transition: opacity 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
}
.MuiInputBase-input:-ms-input-placeholder {
  color: currentColor;
  opacity: 0.42;
  transition: opacity 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
}
.MuiInputBase-input::-ms-input-placeholder {
  color: currentColor;
  opacity: 0.42;
  transition: opacity 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
}
.MuiInputBase-input:focus {
  outline: 0;
}
.MuiInputBase-input:invalid {
  box-shadow: none;
}
.MuiInputBase-input::-webkit-search-decoration {
  -webkit-appearance: none;
}
.MuiInputBase-input.Mui-disabled {
  opacity: 1;
}
.MuiInputBase-input:-webkit-autofill {
  animation-name: mui-auto-fill;
  animation-duration: 5000s;
}
label[data-shrink=false] + .MuiInputBase-formControl .MuiInputBase-input::-webkit-input-placeholder {
  opacity: 0 !important;
}
label[data-shrink=false] + .MuiInputBase-formControl .MuiInputBase-input::-moz-placeholder {
  opacity: 0 !important;
}
label[data-shrink=false] + .MuiInputBase-formControl .MuiInputBase-input:-ms-input-placeholder {
  opacity: 0 !important;
}
label[data-shrink=false] + .MuiInputBase-formControl .MuiInputBase-input::-ms-input-placeholder {
  opacity: 0 !important;
}
label[data-shrink=false] + .MuiInputBase-formControl .MuiInputBase-input:focus::-webkit-input-placeholder {
  opacity: 0.42;
}
label[data-shrink=false] + .MuiInputBase-formControl .MuiInputBase-input:focus::-moz-placeholder {
  opacity: 0.42;
}
label[data-shrink=false] + .MuiInputBase-formControl .MuiInputBase-input:focus:-ms-input-placeholder {
  opacity: 0.42;
}
label[data-shrink=false] + .MuiInputBase-formControl .MuiInputBase-input:focus::-ms-input-placeholder {
  opacity: 0.42;
}
.MuiInputBase-inputMarginDense {
  padding-top: 3px;
}
.MuiInputBase-inputMultiline {
  height: auto;
  resize: none;
  padding: 0;
}
.MuiInputBase-inputTypeSearch {
  -moz-appearance: textfield;
  -webkit-appearance: textfield;
}
</style><style data-jss="" data-meta="MuiFormControl">
.MuiFormControl-root {
  border: 0;
  margin: 0;
  display: inline-flex;
  padding: 0;
  position: relative;
  min-width: 0;
  flex-direction: column;
  vertical-align: top;
}
.MuiFormControl-marginNormal {
  margin-top: 16px;
  margin-bottom: 8px;
}
.MuiFormControl-marginDense {
  margin-top: 8px;
  margin-bottom: 4px;
}
.MuiFormControl-fullWidth {
  width: 100%;
}
</style><style data-jss="" data-meta="MuiLinearProgress">
.MuiLinearProgress-root {
  height: 4px;
  overflow: hidden;
  position: relative;
}
@media print {
  .MuiLinearProgress-root {
    -webkit-print-color-adjust: exact;
  }
}
.MuiLinearProgress-colorPrimary {
  background-color: rgb(182, 188, 226);
}
.MuiLinearProgress-colorSecondary {
  background-color: rgb(251, 158, 191);
}
.MuiLinearProgress-buffer {
  background-color: transparent;
}
.MuiLinearProgress-query {
  transform: rotate(180deg);
}
.MuiLinearProgress-dashed {
  width: 100%;
  height: 100%;
  position: absolute;
  animation: MuiLinearProgress-keyframes-buffer 3s infinite linear;
  margin-top: 0;
}
.MuiLinearProgress-dashedColorPrimary {
  background-size: 10px 10px;
  background-image: radial-gradient(rgb(182, 188, 226) 0%, rgb(182, 188, 226) 16%, transparent 42%);
  background-position: 0 -23px;
}
.MuiLinearProgress-dashedColorSecondary {
  background-size: 10px 10px;
  background-image: radial-gradient(rgb(251, 158, 191) 0%, rgb(251, 158, 191) 16%, transparent 42%);
  background-position: 0 -23px;
}
.MuiLinearProgress-bar {
  top: 0;
  left: 0;
  width: 100%;
  bottom: 0;
  position: absolute;
  transition: transform 0.2s linear;
  transform-origin: left;
}
.MuiLinearProgress-barColorPrimary {
  background-color: #3f51b5;
}
.MuiLinearProgress-barColorSecondary {
  background-color: #f50057;
}
.MuiLinearProgress-bar1Indeterminate {
  width: auto;
  animation: MuiLinearProgress-keyframes-indeterminate1 2.1s cubic-bezier(0.65, 0.815, 0.735, 0.395) infinite;
}
.MuiLinearProgress-bar1Determinate {
  transition: transform .4s linear;
}
.MuiLinearProgress-bar1Buffer {
  z-index: 1;
  transition: transform .4s linear;
}
.MuiLinearProgress-bar2Indeterminate {
  width: auto;
  animation: MuiLinearProgress-keyframes-indeterminate2 2.1s cubic-bezier(0.165, 0.84, 0.44, 1) 1.15s infinite;
}
.MuiLinearProgress-bar2Buffer {
  transition: transform .4s linear;
}
@-webkit-keyframes MuiLinearProgress-keyframes-indeterminate1 {
  0% {
    left: -35%;
    right: 100%;
  }
  60% {
    left: 100%;
    right: -90%;
  }
  100% {
    left: 100%;
    right: -90%;
  }
}
@-webkit-keyframes MuiLinearProgress-keyframes-indeterminate2 {
  0% {
    left: -200%;
    right: 100%;
  }
  60% {
    left: 107%;
    right: -8%;
  }
  100% {
    left: 107%;
    right: -8%;
  }
}
@-webkit-keyframes MuiLinearProgress-keyframes-buffer {
  0% {
    opacity: 1;
    background-position: 0 -23px;
  }
  50% {
    opacity: 0;
    background-position: 0 -23px;
  }
  100% {
    opacity: 1;
    background-position: -200px -23px;
  }
}
</style><style data-jss="" data-meta="MuiPopover">
.MuiPopover-paper {
  outline: 0;
  position: absolute;
  max-width: calc(100% - 32px);
  min-width: 16px;
  max-height: calc(100% - 32px);
  min-height: 16px;
  overflow-x: hidden;
  overflow-y: auto;
}
</style><style data-jss="" data-meta="MuiMenu">
.MuiMenu-paper {
  max-height: calc(100% - 96px);
  -webkit-overflow-scrolling: touch;
}
.MuiMenu-list {
  outline: 0;
}
</style><style data-jss="" data-meta="PrivateNotchedOutline">
.jss264 {
  top: -5px;
  left: 0;
  right: 0;
  bottom: 0;
  margin: 0;
  padding: 0 8px;
  overflow: hidden;
  position: absolute;
  border-style: solid;
  border-width: 1px;
  border-radius: inherit;
  pointer-events: none;
}
.jss265 {
  padding: 0;
  text-align: left;
  transition: width 150ms cubic-bezier(0.0, 0, 0.2, 1) 0ms;
  line-height: 11px;
}
.jss266 {
  width: auto;
  height: 11px;
  display: block;
  padding: 0;
  font-size: 0.75em;
  max-width: 0.01px;
  text-align: left;
  transition: max-width 50ms cubic-bezier(0.0, 0, 0.2, 1) 0ms;
  visibility: hidden;
}
.jss266 > span {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
.jss267 {
  max-width: 1000px;
  transition: max-width 100ms cubic-bezier(0.0, 0, 0.2, 1) 50ms;
}
</style><style data-jss="" data-meta="MuiOutlinedInput">
.MuiOutlinedInput-root {
  position: relative;
  border-radius: 4px;
}
.MuiOutlinedInput-root:hover .MuiOutlinedInput-notchedOutline {
  border-color: rgba(0, 0, 0, 0.87);
}
@media (hover: none) {
  .MuiOutlinedInput-root:hover .MuiOutlinedInput-notchedOutline {
    border-color: rgba(0, 0, 0, 0.23);
  }
}
.MuiOutlinedInput-root.Mui-focused .MuiOutlinedInput-notchedOutline {
  border-color: #3f51b5;
  border-width: 2px;
}
.MuiOutlinedInput-root.Mui-error .MuiOutlinedInput-notchedOutline {
  border-color: #f44336;
}
.MuiOutlinedInput-root.Mui-disabled .MuiOutlinedInput-notchedOutline {
  border-color: rgba(0, 0, 0, 0.26);
}
.MuiOutlinedInput-colorSecondary.Mui-focused .MuiOutlinedInput-notchedOutline {
  border-color: #f50057;
}
.MuiOutlinedInput-adornedStart {
  padding-left: 14px;
}
.MuiOutlinedInput-adornedEnd {
  padding-right: 14px;
}
.MuiOutlinedInput-multiline {
  padding: 18.5px 14px;
}
.MuiOutlinedInput-multiline.MuiOutlinedInput-marginDense {
  padding-top: 10.5px;
  padding-bottom: 10.5px;
}
.MuiOutlinedInput-notchedOutline {
  border-color: rgba(0, 0, 0, 0.23);
}
.MuiOutlinedInput-input {
  padding: 18.5px 14px;
}
.MuiOutlinedInput-input:-webkit-autofill {
  border-radius: inherit;
}
.MuiOutlinedInput-inputMarginDense {
  padding-top: 10.5px;
  padding-bottom: 10.5px;
}
.MuiOutlinedInput-inputMultiline {
  padding: 0;
}
.MuiOutlinedInput-inputAdornedStart {
  padding-left: 0;
}
.MuiOutlinedInput-inputAdornedEnd {
  padding-right: 0;
}
</style><style data-jss="" data-meta="MuiSelect">
.MuiSelect-select {
  cursor: pointer;
  min-width: 16px;
  user-select: none;
  border-radius: 0;
  -moz-appearance: none;
  -webkit-appearance: none;
}
.MuiSelect-select:focus {
  border-radius: 0;
  background-color: rgba(0, 0, 0, 0.05);
}
.MuiSelect-select::-ms-expand {
  display: none;
}
.MuiSelect-select.Mui-disabled {
  cursor: default;
}
.MuiSelect-select[multiple] {
  height: auto;
}
.MuiSelect-select:not([multiple]) option, .MuiSelect-select:not([multiple]) optgroup {
  background-color: #fff;
}
.MuiSelect-select.MuiSelect-select {
  padding-right: 24px;
}
.MuiSelect-filled.MuiSelect-filled {
  padding-right: 32px;
}
.MuiSelect-outlined {
  border-radius: 4px;
}
.MuiSelect-outlined.MuiSelect-outlined {
  padding-right: 32px;
}
.MuiSelect-selectMenu {
  height: auto;
  overflow: hidden;
  min-height: 1.1876em;
  white-space: nowrap;
  text-overflow: ellipsis;
}
.MuiSelect-icon {
  top: calc(50% - 12px);
  color: rgba(0, 0, 0, 0.54);
  right: 0;
  position: absolute;
  pointer-events: none;
}
.MuiSelect-icon.Mui-disabled {
  color: rgba(0, 0, 0, 0.26);
}
.MuiSelect-iconOpen {
  transform: rotate(180deg);
}
.MuiSelect-iconFilled {
  right: 7px;
}
.MuiSelect-iconOutlined {
  right: 7px;
}
.MuiSelect-nativeInput {
  left: 0;
  width: 100%;
  bottom: 0;
  opacity: 0;
  position: absolute;
  pointer-events: none;
}
</style><style data-jss="" data-meta="MuiTab">
.MuiTab-root {
  padding: 6px 12px;
  overflow: hidden;
  position: relative;
  font-size: 0.875rem;
  max-width: 264px;
  min-width: 72px;
  box-sizing: border-box;
  min-height: 48px;
  text-align: center;
  flex-shrink: 0;
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 500;
  line-height: 1.75;
  white-space: normal;
  letter-spacing: 0.02857em;
  text-transform: uppercase;
}
@media (min-width:600px) {
  .MuiTab-root {
    min-width: 160px;
  }
}
.MuiTab-root.Mui-selected {
  font-weight: 600 !important;
  border-bottom: 2.8px solid #4079DA;
}
.MuiTab-labelIcon {
  min-height: 72px;
  padding-top: 9px;
}
.MuiTab-labelIcon .MuiTab-wrapper > *:first-child {
  margin-bottom: 6px;
}
.MuiTab-textColorInherit {
  color: inherit;
  opacity: 0.7;
}
.MuiTab-textColorInherit.Mui-selected {
  opacity: 1;
}
.MuiTab-textColorInherit.Mui-disabled {
  opacity: 0.5;
}
.MuiTab-textColorPrimary {
  color: rgba(0, 0, 0, 0.54);
}
.MuiTab-textColorPrimary.Mui-selected {
  color: #3f51b5;
}
.MuiTab-textColorPrimary.Mui-disabled {
  color: rgba(0, 0, 0, 0.38);
}
.MuiTab-textColorSecondary {
  color: rgba(0, 0, 0, 0.54);
}
.MuiTab-textColorSecondary.Mui-selected {
  color: #f50057;
}
.MuiTab-textColorSecondary.Mui-disabled {
  color: rgba(0, 0, 0, 0.38);
}
.MuiTab-fullWidth {
  flex-grow: 1;
  max-width: none;
  flex-basis: 0;
  flex-shrink: 1;
}
.MuiTab-wrapped {
  font-size: 0.75rem;
  line-height: 1.5;
}
.MuiTab-wrapper {
  width: 100%;
  display: block;
  overflow: hidden;
  align-items: center;
  white-space: nowrap;
  text-overflow: ellipsis;
  flex-direction: column;
  justify-content: center;
}
</style><style data-jss="" data-meta="PrivateTabIndicator">
.jss259 {
  width: 100%;
  bottom: 0;
  height: 2px;
  position: absolute;
  transition: all 300ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
}
.jss260 {
  background-color: #3f51b5;
}
.jss261 {
  background-color: #f50057;
}
.jss262 {
  right: 0;
  width: 2px;
  height: 100%;
}
</style><style data-jss="" data-meta="MuiTabs">
.MuiTabs-root {
  display: flex;
  overflow: hidden;
  min-height: 48px;
  -webkit-overflow-scrolling: touch;
}
.MuiTabs-vertical {
  flex-direction: column;
}
.MuiTabs-flexContainer {
  display: flex;
}
.MuiTabs-flexContainerVertical {
  flex-direction: column;
}
.MuiTabs-centered {
  justify-content: center;
}
.MuiTabs-scroller {
  flex: 1 1 auto;
  display: inline-block;
  position: relative;
  white-space: nowrap;
}
.MuiTabs-fixed {
  width: 100%;
  overflow-x: hidden;
}
.MuiTabs-scrollable {
  overflow-x: scroll;
  scrollbar-width: none;
}
.MuiTabs-scrollable::-webkit-scrollbar {
  display: none;
}
@media (max-width:599.95px) {
  .MuiTabs-scrollButtonsDesktop {
    display: none;
  }
}
.MuiTabs-indicator {
  display: none;
}
</style><style data-jss="" data-meta="MuiTooltip">
.MuiTooltip-popper {
  z-index: 1500;
  pointer-events: none;
}
.MuiTooltip-popperInteractive {
  pointer-events: auto;
}
.MuiTooltip-popperArrow[x-placement*="bottom"] .MuiTooltip-arrow {
  top: 0;
  left: 0;
  margin-top: -0.71em;
  margin-left: 4px;
  margin-right: 4px;
}
.MuiTooltip-popperArrow[x-placement*="top"] .MuiTooltip-arrow {
  left: 0;
  bottom: 0;
  margin-left: 4px;
  margin-right: 4px;
  margin-bottom: -0.71em;
}
.MuiTooltip-popperArrow[x-placement*="right"] .MuiTooltip-arrow {
  left: 0;
  width: 0.71em;
  height: 1em;
  margin-top: 4px;
  margin-left: -0.71em;
  margin-bottom: 4px;
}
.MuiTooltip-popperArrow[x-placement*="left"] .MuiTooltip-arrow {
  right: 0;
  width: 0.71em;
  height: 1em;
  margin-top: 4px;
  margin-right: -0.71em;
  margin-bottom: 4px;
}
.MuiTooltip-popperArrow[x-placement*="left"] .MuiTooltip-arrow::before {
  transform-origin: 0 0;
}
.MuiTooltip-popperArrow[x-placement*="right"] .MuiTooltip-arrow::before {
  transform-origin: 100% 100%;
}
.MuiTooltip-popperArrow[x-placement*="top"] .MuiTooltip-arrow::before {
  transform-origin: 100% 0;
}
.MuiTooltip-popperArrow[x-placement*="bottom"] .MuiTooltip-arrow::before {
  transform-origin: 0 100%;
}
.MuiTooltip-tooltip {
  color: #fff;
  padding: 4px 8px;
  font-size: 0.625rem;
  max-width: 300px;
  word-wrap: break-word;
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 500;
  line-height: 1.4em;
  border-radius: 4px;
  background-color: rgba(97, 97, 97, 0.9);
}
.MuiTooltip-tooltipArrow {
  margin: 0;
  position: relative;
}
.MuiTooltip-arrow {
  color: rgba(97, 97, 97, 0.9);
  width: 1em;
  height: 0.71em;
  overflow: hidden;
  position: absolute;
  box-sizing: border-box;
}
.MuiTooltip-arrow::before {
  width: 100%;
  height: 100%;
  margin: auto;
  content: "";
  display: block;
  transform: rotate(45deg);
  background-color: currentColor;
}
.MuiTooltip-touch {
  padding: 8px 16px;
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.14286em;
}
.MuiTooltip-tooltipPlacementLeft {
  margin: 0 24px ;
  transform-origin: right center;
}
@media (min-width:600px) {
  .MuiTooltip-tooltipPlacementLeft {
    margin: 0 14px;
  }
}
.MuiTooltip-tooltipPlacementRight {
  margin: 0 24px;
  transform-origin: left center;
}
@media (min-width:600px) {
  .MuiTooltip-tooltipPlacementRight {
    margin: 0 14px;
  }
}
.MuiTooltip-tooltipPlacementTop {
  margin: 24px 0;
  transform-origin: center bottom;
}
@media (min-width:600px) {
  .MuiTooltip-tooltipPlacementTop {
    margin: 14px 0;
  }
}
.MuiTooltip-tooltipPlacementBottom {
  margin: 24px 0;
  transform-origin: center top;
}
@media (min-width:600px) {
  .MuiTooltip-tooltipPlacementBottom {
    margin: 14px 0;
  }
}
</style><style data-jss="" data-meta="makeStyles">
.jss256 {
  color: #000;
}
.jss257 {
  background-color: #000;
}
</style><style data-jss="" data-meta="makeStyles">
.jss18 {
  width: 100%;
  margin: 0;
  max-width: 656px !important;
}
@media (max-width:965px) {
  .jss18 {
    scale: 100%;
    margin: 0;
    max-height: 100%;
  }
}
</style><style data-jss="" data-meta="makeStyles">
.jss24 {
  width: 100%;
  margin: 0;
  max-width: 656px !important;
}
@media (max-width:965px) {
  .jss24 {
    scale: 100%;
    margin: 0;
    max-height: 100%;
  }
}
</style><style data-jss="" data-meta="makeStyles">
.jss215 {
  width: 100%;
  margin: 0;
  max-width: 656px !important;
}
@media (max-width:965px) {
  .jss215 {
    scale: 100%;
    margin: 0;
    max-height: 100%;
  }
}
</style><style data-jss="" data-meta="makeStyles">
.jss221 {
  width: 100%;
  margin: 0;
  max-width: 656px !important;
}
@media (max-width:965px) {
  .jss221 {
    scale: 100%;
    margin: 0;
    max-height: 100%;
  }
}
</style><style data-jss="" data-meta="makeStyles">
.jss249 {
  width: 100%;
  margin: 0;
  max-width: 656px !important;
}
@media (max-width:965px) {
  .jss249 {
    scale: 100%;
    margin: 0;
    max-height: 100%;
  }
}
</style><style data-jss="" data-meta="makeStyles">
.jss255 {
  display: revert;
  padding: 0px;
  border-radius: 8px;
}
</style><style data-jss="" data-meta="makeStyles">
.jss250 {
  background: none;
  box-shadow: none;
  transition: min-height 150ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,background-color 150ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;;
}
</style><style data-jss="" data-meta="makeStyles">
.jss251 {
  gap: 12px;
  padding: 12px 0;
  min-height: fit-content;
  transition: min-height 150ms cubic-bezier(0.4, 0, 0.2, 1) 0ms,background-color 150ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;;
  flex-direction: row-reverse;
}
.jss251.jss254 {
  min-height: fit-content;
}
.jss251:hover {
  background: #22242E;
}
.jss252 {
  gap: 25px;
  margin: 0;
}
.jss252.jss254 {
  margin: 0;
}
.jss253 {
  padding: 0;
  transform: rotate(270deg);
  margin-right: 0;
}
.jss253.jss254 {
  transform: rotate(360deg);
}
</style><style data-jss="" data-meta="makeStyles">
.jss704 {
  padding: 0;
  min-height: fit-content;
}
.jss704.jss707 {
  min-height: fit-content;
}
.jss705 {
  margin: 0;
}
.jss705.jss707 {
  margin: 0;
}
.jss706 {
  padding: 0;
  margin-right: 0;
}
</style><style data-jss="" data-meta="makeStyles">
.jss703 {
  width: 100%;
  margin: 0;
  max-width: 656px !important;
}
@media (max-width:965px) {
  .jss703 {
    scale: 100%;
    margin: 0;
    max-height: 100%;
  }
}
</style><style type="text/css">.alert-box p { font-size: 16px; }</style><link rel="modulepreload" as="script" crossorigin="" href="https://static.codechef.com/build/react2/assets/TopBanner-bMTAInVb.js"><link rel="modulepreload" as="script" crossorigin="" href="https://static.codechef.com/build/react2/assets/react-csv-IA6T4-yP.js"><link rel="modulepreload" as="script" crossorigin="" href="https://static.codechef.com/build/react2/assets/BreadCrumbs-hdRjKpvl.js"><link rel="stylesheet" href="./cric12_files/BreadCrumbs-owLrRhir.css"><link rel="modulepreload" as="script" crossorigin="" href="https://static.codechef.com/build/react2/assets/Constants-A5ABrCIs.js"><link rel="modulepreload" as="script" crossorigin="" href="https://static.codechef.com/build/react2/assets/prism-vs-dark-MS2_IotO.js"><link rel="modulepreload" as="script" crossorigin="" href="https://static.codechef.com/build/react2/assets/rehype-katex-h-qQbLMn.js"><link rel="stylesheet" href="./cric12_files/prism-vs-dark-XENCowIx.css"><link rel="modulepreload" as="script" crossorigin="" href="https://static.codechef.com/build/react2/assets/ace-builds-10Ji70GH.js"><link rel="modulepreload" as="script" crossorigin="" href="https://static.codechef.com/build/react2/assets/index-XLj1PShD.js"><link rel="modulepreload" as="script" crossorigin="" href="https://static.codechef.com/build/react2/assets/HorizontalTabPanel-QZG8n049.js"><link rel="stylesheet" href="./cric12_files/HorizontalTabPanel-lgAHSzkT.css"><link rel="modulepreload" as="script" crossorigin="" href="https://static.codechef.com/build/react2/assets/katex-sKQXyiPV.js"><link rel="stylesheet" href="./cric12_files/katex-a6DLCiel.css"><link rel="modulepreload" as="script" crossorigin="" href="https://static.codechef.com/build/react2/assets/UserStar-2xB5OScq.js"><link rel="stylesheet" href="./cric12_files/UserStar-xD-l1Tmd.css"><link rel="modulepreload" as="script" crossorigin="" href="https://static.codechef.com/build/react2/assets/SelectDropdown-uTOTRYNG.js"><link rel="stylesheet" href="./cric12_files/SelectDropdown-vs4kBCgD.css"><link rel="modulepreload" as="script" crossorigin="" href="https://static.codechef.com/build/react2/assets/prismjs-5PdtpHlj.js"><link rel="modulepreload" as="script" crossorigin="" href="https://static.codechef.com/build/react2/assets/Constant-MIgd2H8z.js"><link rel="modulepreload" as="script" crossorigin="" href="https://static.codechef.com/build/react2/assets/TablePagination-Jh9ESDK-.js"><link rel="stylesheet" href="./cric12_files/TablePagination-Gbyk7yFc.css"><link rel="modulepreload" as="script" crossorigin="" href="https://static.codechef.com/build/react2/assets/DataGrid-3Vu_EJOL.js"><link rel="modulepreload" as="script" crossorigin="" href="https://static.codechef.com/build/react2/assets/index.es-ubZHsp0R.js"><link rel="stylesheet" href="./cric12_files/TopBanner-Snv9fKFc.css"><script src="./cric12_files/mode-plain_text.js.download"></script><script src="./cric12_files/mode-python.js.download"></script><script src="./cric12_files/python.js.download"></script></head>

<body style="background: rgb(29, 30, 35);">
  <noscript>You need to enable JavaScript to run this app.</noscript>
  <div id="root" class="no-print"><div style="background: rgb(29, 30, 35);"><div class="MuiBackdrop-root _backdrop_pm713_1 undefined" aria-hidden="true" style="opacity: 0; visibility: hidden;"><div class="MuiLinearProgress-root MuiLinearProgress-colorPrimary _progress_pm713_7 MuiLinearProgress-indeterminate" role="progressbar"><div class="MuiLinearProgress-bar MuiLinearProgress-barColorPrimary MuiLinearProgress-bar1Indeterminate"></div><div class="MuiLinearProgress-bar MuiLinearProgress-bar2Indeterminate MuiLinearProgress-barColorPrimary"></div></div></div><div class="_pageContainer_1se0b_3 _dark_1se0b_9" style="max-width: 100%;"><div style="display: block;"><div class="_sidebarContainer_6xw4t_2 _dark_6xw4t_29 "><div class="_sidebarContainer_1ohcw_2 _dark_1ohcw_209 notranslate"><div class="_sidebarHeader_1ohcw_5"><div class="_syllabusContainer_1ohcw_26"><div class="_syllabusInfo_1ohcw_42"><img alt="learn-icon" src="./cric12_files/basic-programming-concepts.svg" loading="lazy"><div class="_syllabusNameContainer_1ohcw_46"><div class="_syllabusName_1ohcw_46">500 difficulty rating</div><div class="_viewSyllabusLink_1ohcw_57"><a class="_link_1ohcw_57 _hoverClass_2pyv4_10" href="https://www.codechef.com/practice/basic-programming-concepts" target="_blank" rel="noopener noreferrer">View full syllabus<span class="_icon__container_1ohcw_68"><svg class="MuiSvgIcon-root _icon_1ohcw_68" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5v2h6.59L4 18.59 5.41 20 17 8.41V15h2V5z"></path></svg></span></a></div></div></div><div class="_sidebarCloseIconContainer_1ohcw_31"><svg class="MuiSvgIcon-root _sidebarCloseIcon_1ohcw_31" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path></svg></div></div><div class="_progress_1ohcw_13"><div class="_fill_1ohcw_21" style="width: 0%;"></div></div><div class="_percentageCompleted_1ohcw_5">0% Completed</div></div><div class="_sidebarContent_1ohcw_92"><div class="_modules_1ohcw_105"><div class="MuiPaper-root MuiAccordion-root jss250 Mui-expanded MuiAccordion-rounded MuiPaper-elevation1 MuiPaper-rounded"><div class="MuiButtonBase-root MuiAccordionSummary-root jss251 Mui-expanded jss254" tabindex="0" role="button" aria-disabled="false" aria-expanded="true" aria-controls="panel1a-content" id="panel1a-header"><div class="MuiAccordionSummary-content jss252 Mui-expanded jss254"><div class="_moduleTitle_1ohcw_105"><span>Less than 500 difficulty rating</span></div></div><div class="MuiButtonBase-root MuiIconButton-root MuiAccordionSummary-expandIcon jss253 Mui-expanded jss254 MuiIconButton-edgeEnd" aria-disabled="false" aria-hidden="true"><span class="MuiIconButton-label"><svg class="MuiSvgIcon-root _expandIcon_1ohcw_129" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M16.59 8.59L12 13.17 7.41 8.59 6 10l6 6 6-6z"></path></svg></span><span class="MuiTouchRipple-root"></span></div></div><div class="MuiCollapse-container MuiCollapse-entered" style="min-height: 0px;"><div class="MuiCollapse-wrapper"><div class="MuiCollapse-wrapperInner"><div aria-labelledby="panel1a-header" id="panel1a-content" role="region"><div class="MuiAccordionDetails-root jss255"><div class="_submoduleSummary_1ohcw_146"><div class="_modules_1ohcw_105" style="padding-left: 30px;"><div class="MuiPaper-root MuiAccordion-root jss250 Mui-expanded MuiAccordion-rounded MuiPaper-elevation1 MuiPaper-rounded"><div class="MuiButtonBase-root MuiAccordionSummary-root jss251 Mui-expanded jss254" tabindex="0" role="button" aria-disabled="false" aria-expanded="true" aria-controls="panel1a-content" id="panel1a-header"><div class="MuiAccordionSummary-content jss252 Mui-expanded jss254"><div class="_moduleTitle_1ohcw_105"><span class="_moduleName_1ohcw_167">Less than 500</span><span></span></div></div></div><div class="MuiCollapse-container MuiCollapse-entered" style="min-height: 0px;"><div class="MuiCollapse-wrapper"><div class="MuiCollapse-wrapperInner"><div aria-labelledby="panel1a-header" id="panel1a-content" role="region"><div class="MuiAccordionDetails-root jss255"><div class="_submoduleSummary_1ohcw_146"><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CWC23QUALIF"><div class="_innerRow_1ohcw_153" style="background: rgb(46, 52, 70);"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Cricket World Cup Qualifier</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/LUCKYSEVEN"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Lucky Seven</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CLEARDAY"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Clear Day</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/DOUBLERENT"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Double Rent</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/TAXSAVING"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Saving Taxes</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/TOP10"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Masterchef finals</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/BIRYANI"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Biryani classes</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/LUDO"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Chef Plays Ludo</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/PRACLIST"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">How many unattempted problems</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/DETSCORE"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Determine the Score</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/ERROR404"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">404 Not Found</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/OFFBY1"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Off By One</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/DONDRIVE"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Donation Drive</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/KITCHENTIME"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Kitchen Timings</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/IPLTRSH"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">IPL Ticket Rush</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/AUDIBLE"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Audible Range</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/TIMELY"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Reach on Time</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/PUZHUNT"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Puzzle Hunt</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/BNE_APT"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Bone Appetit</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/TALLER"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Who is taller!</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/REACHTARGET"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Reach the Target</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/BESTOFTWO"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Best of Two</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/RIP2000"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">2000</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/MINHEIGHT"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Roller Coaster</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CANDIVIDE"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Candy Division</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CHEFONDATE"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Chef On Date</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/PAR2"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Parity</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/PRIZEPOOL"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Total Prize Money</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CNTWRD"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Counting Words</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/BTRYHLTH"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Battery Health</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/JERRYCHASE"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Tom and Jerry Chase</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/AGEING"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Ageing</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/RIGHTTHERE"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Right There</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SNDMAX"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Second Max of Three Numbers</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/BULLBEAR"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Bull or Bear</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/FOURTICKETS"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Four Tickets</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CHAIRS_"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Chairs Requirement</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/DNATION"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Chef and Donation</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SUMM"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Sum it</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SUBSCRIBE"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Get Subscription</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/MVR"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Messi vs Ronaldo</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/WAITTIME"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Waiting Time</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/OCTATHON"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">October Marathon</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/ONEMORE"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Just One More Episode</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/MANAPTS"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Mana Points</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/RAINFALL1"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Rain in Chefland</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/AUCTION"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Bidding</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/FINE"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Overspeeding Fine</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CHESSTIME"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Chess Time</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/FAIRPASS"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Passes for Fair</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/READPAGES"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Read Pages</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/COUGAME"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Couple Game</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/AIRINDEX"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Air Quality Index</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/FEVER"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Fever</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SLEEP"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Sleep deprivation</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/M1ENROL"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">MATH1 Enrolment</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SEMCOURSES"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Chef and Chapters</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/WATERREQ"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Water Requirement</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/LTIME"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Lunchtime</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/INVESTMENT"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Good Investment or Not</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/POPULATION"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Final Population</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/PARTY2"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Chef gives Party</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/COMPLEXITY"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Time Complexity</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/INTRDSGN"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Interior Design</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CARTRIP"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Car Trip</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/TABLETS"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Multivitamin Tablets</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SIXFRIENDS"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Six Friends</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CWIREFRAME"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Chef and Wire Frames</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/MINCOINSREQ"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Minimum Coins</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/KITCHENSPICE"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Spice Level</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CS2023_GIFT"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">The Gift</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/REACH_HOME"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Reach Home</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/DOREWARD"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Donation Rewards</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/TFPAPER"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">True and False Paper</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CABS"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">The Cheaper Cab</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/DISCNT"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Discount</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/HEIGHTRATION"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Height of Rationals</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/INSTAGRAM"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Instagram</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/VOLCONTROL"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Volume Control</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/HS08TEST"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">ATM</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/HOTCOLD"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Is it hot or cold</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/PROINC"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Profit Increment</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/FBC"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Fill the Bucket</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/PARLIAMENT"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Parliament</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/FLOW002"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Find Remainder</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/MANIPULATE"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Ezio and Guards</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CMASKS"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Chef and Masks</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SPECIALITY"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Speciality</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/MAXIMUMSUBS"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Maximum Submissions</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/TVDISC"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">TV Discount</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/BROKENPHONE"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Broken Phone</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/TYRE"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Tyre problem</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/FLOW006"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Sum of Digits</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/BUDGET_"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Monthly Budget</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CREDSCORE"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Credit score</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/FLOW004"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">First and Last Digit</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/INTEST"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Enormous Input Test</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/PRACTICEPERF"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Practice makes us perfect</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/ASSIGNMNT"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Pending Assignments</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/COURSEREG"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Course Registration</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/INSURANCE"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Insurance</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/AIRLINES"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Codechef Airlines</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/INCRIQ"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Increase IQ</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/BATTERYLOW"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Battery Low</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/BOBBANK"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Bob at the Bank</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/MANGOES"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">The Mango Truck</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/MONOPOLY"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Monopoly in Chefland</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/WATERFLOW"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Bucket and Water Flow </span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/F1RULE"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Miami GP</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/DOMINANT"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Dominant Army</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SONGS"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Playlist</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CHEFCHOCO"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Chef and Chocolates</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/NETFLIX"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Netflix</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CGYM"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Chef and Gym</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a><a href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CHEAPFOOD"><div class="_innerRow_1ohcw_153"><div class="_lessonType_1ohcw_160"><span class="_moduleName_1ohcw_167">Best Coupon</span><span><i class="_status__icon_1ohcw_188"></i></span></div></div></a></div></div></div></div></div></div></div></div></div></div></div></div></div></div></div></div></div></div></div><div class="_learningContest__container_lvmtf_2 _dark_lvmtf_29"><div class="_navigate-button__container_lvmtf_8 notranslate _banner__container_lvmtf_208"><div class="_navigation-left-wrapper_lvmtf_14"><div class="_sideNavigationContainer_lvmtf_212"><a href="https://www.codechef.com/practice/basic-programming-concepts" aria-label="Back to practice"><div class="_icon__container_lvmtf_98"><svg class="MuiSvgIcon-root _icon_lvmtf_58" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"></path></svg></div></a><i class="_hamburgerIcon_lvmtf_223 _dark_lvmtf_29"></i></div><div class="_difficultyRatings__box_lvmtf_217 _dark_lvmtf_29"><span>Difficulty: &nbsp;</span><span class="_value_lvmtf_32 _dark_lvmtf_29">203</span></div><div class="_darkModeContainer_2m751_2 _dark_2m751_2" title="Switch to Light Mode" style="margin-left: 0px;"><svg class="MuiSvgIcon-root _sunIcon_2m751_22 _dark_2m751_2" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M6.76 4.84l-1.8-1.79-1.41 1.41 1.79 1.79 1.42-1.41zM4 10.5H1v2h3v-2zm9-9.95h-2V3.5h2V.55zm7.45 3.91l-1.41-1.41-1.79 1.79 1.41 1.41 1.79-1.79zm-3.21 13.7l1.79 1.8 1.41-1.41-1.8-1.79-1.4 1.4zM20 10.5v2h3v-2h-3zm-8-5c-3.31 0-6 2.69-6 6s2.69 6 6 6 6-2.69 6-6-2.69-6-6-6zm-1 16.95h2V19.5h-2v2.95zm-7.45-3.91l1.41 1.41 1.79-1.8-1.41-1.41-1.79 1.8z"></path></svg></div><div class="_bookmark_yz1ej_2"><hr class="MuiDivider-root _divider_yz1ej_74 _dark_yz1ej_26 MuiDivider-flexItem MuiDivider-vertical"><div class="_bookmarkIcon_yz1ej_16" title="Add to bookmark"><i class="_bookmarkOutlined_yz1ej_30 _dark_yz1ej_26"></i></div></div><div class="_stopWatch_y1la1_2"><i class="_stopWatch__icons_y1la1_20" title="Start Timer"><svg class="MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M15 1H9v2h6V1zm-4 13h2V8h-2v6zm8.03-6.61l1.42-1.42c-.43-.51-.9-.99-1.41-1.41l-1.42 1.42C16.07 4.74 14.12 4 12 4c-4.97 0-9 4.03-9 9s4.02 9 9 9 9-4.03 9-9c0-2.12-.74-4.07-1.97-5.61zM12 20c-3.87 0-7-3.13-7-7s3.13-7 7-7 7 3.13 7 7-3.13 7-7 7z"></path></svg></i></div></div><div class="_navigation-button__box_lvmtf_82"><a class="_previous__container_lvmtf_85 _disabled_lvmtf_203" href="https://www.codechef.com/practice/course/basic-programming-concepts/undefined/problems/undefined"><div class="_icon__container_lvmtf_98"><svg class="MuiSvgIcon-root _icon_lvmtf_58" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"></path></svg></div><span class="notranslate">Prev module</span></a><div class="_contest__progress_lvmtf_269 _mergedProgressBar_lvmtf_257" title=""><span class="_progress__bar_lvmtf_260 _filled_lvmtf_288"></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span><span class="_progress__bar_lvmtf_260 " title=""></span></div><a class="_next__container_lvmtf_105 " href="https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/LUCKYSEVEN"><span class="notranslate">Next</span><div class="_icon__container_lvmtf_98"><svg class="MuiSvgIcon-root _icon_lvmtf_58" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></svg></div></a></div></div><div class="_submit__container_lvmtf_431"><div class="_split__container_lvmtf_436"><div class="_tabs-wrapper__panel_lvmtf_439" style="width: calc(50% - 2.5px);"><div class="MuiBox-root jss258 _tabPanel_2ap3p_2 _dark_2ap3p_30"><div class="MuiPaper-root notranslate MuiPaper-elevation1 MuiPaper-rounded" style="margin: 0px; box-shadow: none;"><div class="MuiTabs-root _tab__container_lvmtf_463"><div class="MuiTabs-scroller MuiTabs-fixed" style="overflow: hidden;"><div class="MuiTabs-flexContainer" role="tablist"><button class="MuiButtonBase-root MuiTab-root MuiTab-textColorInherit _tab__title_lvmtf_450 _dark_lvmtf_29 Mui-selected" tabindex="0" type="button" role="tab" aria-selected="true" id="vertical-tab-panel-0" aria-controls="vertical-tab-panel-0"><span class="MuiTab-wrapper">Statement</span><span class="MuiTouchRipple-root"></span></button><button class="MuiButtonBase-root MuiTab-root MuiTab-textColorInherit _tab__title_lvmtf_450 _dark_lvmtf_29" tabindex="-1" type="button" role="tab" aria-selected="false" id="vertical-tab-panel-1" aria-controls="vertical-tab-panel-1"><span class="MuiTab-wrapper">Submissions</span><span class="MuiTouchRipple-root"></span></button><button class="MuiButtonBase-root MuiTab-root MuiTab-textColorInherit _tab__title_lvmtf_450 _dark_lvmtf_29" tabindex="-1" type="button" role="tab" aria-selected="false" id="vertical-tab-panel-2" aria-controls="vertical-tab-panel-2"><span class="MuiTab-wrapper">Solution</span><span class="MuiTouchRipple-root"></span></button><button class="MuiButtonBase-root MuiTab-root MuiTab-textColorInherit _tab__title_lvmtf_450 _dark_lvmtf_29" tabindex="-1" type="button" role="tab" aria-selected="false" id="vertical-tab-panel-3" aria-controls="vertical-tab-panel-3"><span class="MuiTab-wrapper">AI Help</span><span class="MuiTouchRipple-root"></span></button></div><span class="jss259 jss260 MuiTabs-indicator" style="left: 0px; width: 160px; background: rgb(90, 134, 220);"></span></div></div></div><div id="vertical-tab-panel-0" aria-labelledby="vertical-tab-panel-0" class="_tab__content_lvmtf_467" style="height: calc(-95px + 100vh);"><div class="MuiBox-root jss263"><div class="_problem-statement__container_jtzpf_2"><div class="_problem-statement__inner__container_jtzpf_107"><div id="problem-statement" class="_problemBody_1x1re_29 _dark_1x1re_239 print "><h3 class="notranslate">Cricket World Cup Qualifier</h3>
<p>The cricket World Cup has started in Chefland. There are many teams participating in the group stage matches. Any team that scores <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>12</mn></mrow><annotation encoding="application/x-tex">12</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.6444em;"></span><span class="mord">12</span></span></span></span></span> or more points in the group stage matches qualifies for the next stage.</p>
<p>You know the score that a particular team has scored in the group stage matches. Determine if the team has qualified for the next stage or not.</p>
<div class="notranslate">
<h3>Input Format</h3>
<p>The first and only line of input consists of an integer <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>X</mi></mrow><annotation encoding="application/x-tex">X</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.6833em;"></span><span class="mord mathnormal" style="margin-right: 0.07847em;">X</span></span></span></span></span> denoting the total points scored by the given team in the group stage matches.</p>
</div><div class="notranslate">
<h3>Output Format</h3>
<p>Output <code>Yes</code>, if the team has qualified for the next stage, and <code>No</code> otherwise.</p>
<p>You may print each character of the string in uppercase or lowercase (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).</p>
</div>
<h3 class="notranslate">Constraints</h3>
<div class="_html_code__block_1x1re_188 notranslate">
<ul>
<li><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>1</mn><mo>≤</mo><mi>X</mi><mo>≤</mo><mn>20</mn></mrow><annotation encoding="application/x-tex">1 \leq X \leq 20</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.7804em; vertical-align: -0.136em;"></span><span class="mord">1</span><span class="mspace" style="margin-right: 0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right: 0.2778em;"></span></span><span class="base"><span class="strut" style="height: 0.8193em; vertical-align: -0.136em;"></span><span class="mord mathnormal" style="margin-right: 0.07847em;">X</span><span class="mspace" style="margin-right: 0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right: 0.2778em;"></span></span><span class="base"><span class="strut" style="height: 0.6444em;"></span><span class="mord">20</span></span></span></span></span></li>
</ul>
</div>
<h3 class="notranslate">Sample 1:</h3>
<div data-reactroot="" class="_input_output__table_1x1re_194 notranslate"><div class="_text_copy__container_1x1re_198"><div class="_text_copy_1x1re_198 _input_top__box_1x1re_211"><span>Input</span><div title="Copy to clipboard" class="undefined" style="pointer-events: all;"><span class="_icon__box_10bs7_2 _dark_10bs7_27 undefined"><i class="_copy__icon_10bs7_14"></i></span></div></div><div class="_text_copy_1x1re_198 _ouput_top__box_1x1re_214"><span>Output</span><div title="Copy to clipboard" class="undefined" style="pointer-events: all;"><span class="_icon__box_10bs7_2 _dark_10bs7_27 undefined"><i class="_copy__icon_10bs7_14"></i></span></div></div></div><div class="_values__container_1x1re_217"><div class="_values_1x1re_217"><pre>3
</pre></div><div class="_values_1x1re_217"><pre>No
</pre></div></div></div>
<h3 class="notranslate">Explanation:</h3>
<div class="notranslate">
<p>The team has not scored <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo>≥</mo><mn>12</mn></mrow><annotation encoding="application/x-tex">\ge 12</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.7719em; vertical-align: -0.136em;"></span><span class="mrel">≥</span><span class="mspace" style="margin-right: 0.2778em;"></span></span><span class="base"><span class="strut" style="height: 0.6444em;"></span><span class="mord">12</span></span></span></span></span> points. Hence it does not qualify.</p>
</div>
<h3 class="notranslate">Sample 2:</h3>
<div data-reactroot="" class="_input_output__table_1x1re_194 notranslate"><div class="_text_copy__container_1x1re_198"><div class="_text_copy_1x1re_198 _input_top__box_1x1re_211"><span>Input</span><div title="Copy to clipboard" class="undefined" style="pointer-events: all;"><span class="_icon__box_10bs7_2 _dark_10bs7_27 undefined"><i class="_copy__icon_10bs7_14"></i></span></div></div><div class="_text_copy_1x1re_198 _ouput_top__box_1x1re_214"><span>Output</span><div title="Copy to clipboard" class="undefined" style="pointer-events: all;"><span class="_icon__box_10bs7_2 _dark_10bs7_27 undefined"><i class="_copy__icon_10bs7_14"></i></span></div></div></div><div class="_values__container_1x1re_217"><div class="_values_1x1re_217"><pre>17
</pre></div><div class="_values_1x1re_217"><pre>Yes
</pre></div></div></div>
<h3 class="notranslate">Explanation:</h3>
<div class="notranslate">
<p>The team has scored <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo>≥</mo><mn>12</mn></mrow><annotation encoding="application/x-tex">\ge 12</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.7719em; vertical-align: -0.136em;"></span><span class="mrel">≥</span><span class="mspace" style="margin-right: 0.2778em;"></span></span><span class="base"><span class="strut" style="height: 0.6444em;"></span><span class="mord">12</span></span></span></span></span> points. Hence it does qualify.</p>
</div></div><div class="_feedback__container_jtzpf_124 notranslate"><div class="_upvoteAnnotationContainer_1hm7m_1237 _dark_1hm7m_1150 "><div class="_upvoteMainContainer_1hm7m_1253"><div class="_upvoteMainContainer_1hm7m_1253"><div class="_upvoteAnnotationHeading_1hm7m_1264 _dark_1hm7m_1150">Did you like the problem?</div><div class="_upvoteAnnotationPara_1hm7m_1296">162 users found this helpful</div></div></div><div class="_reportIcons_1hm7m_1259"><svg class="MuiSvgIcon-root _thumbsUpIcon_1hm7m_1272 _dark_1hm7m_1150" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 21h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-2c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.58 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2zM9 9l4.34-4.34L12 10h9v2l-3 7H9V9zM1 9h4v12H1z"></path></svg><svg class="MuiSvgIcon-root _thumbsDownIcon_1hm7m_1280 _dark_1hm7m_1150" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v2c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm0 12l-4.34 4.34L12 14H3v-2l3-7h9v10zm4-12h4v12h-4z"></path></svg><svg class="MuiSvgIcon-root _commentIcon_1hm7m_1288 _dark_1hm7m_1150" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M21.99 4c0-1.1-.89-2-1.99-2H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h14l4 4-.01-18zM18 14H6v-2h12v2zm0-3H6V9h12v2zm0-3H6V6h12v2z"></path></svg></div></div></div></div></div></div></div><div hidden="" id="vertical-tab-panel-1" aria-labelledby="vertical-tab-panel-1" class="_tab__content_lvmtf_467" style="height: calc(-95px + 100vh);"></div><div hidden="" id="vertical-tab-panel-2" aria-labelledby="vertical-tab-panel-2" class="_tab__content_lvmtf_467" style="height: calc(-95px + 100vh);"></div><div hidden="" id="vertical-tab-panel-3" aria-labelledby="vertical-tab-panel-3" class="_tab__content_lvmtf_467" style="height: calc(-95px + 100vh);"></div></div></div><div class="gutter gutter-horizontal" style="width: 5px;"></div><div class="_ide-wrapper__panel_lvmtf_479 _dark_lvmtf_29 notranslate" style="width: calc(50% - 2.5px);"><div class="_ide_r2w6z_2 _dark_r2w6z_30   notranslate"><div class="_ide__container_r2w6z_6 " style="height: calc(-77px + 100vh);"><div><div class="_ideHeader_15g6v_14 _dark_15g6v_55   "><div><div class="MuiFormControl-root" style="width: 156px;"><div class="MuiInputBase-root MuiOutlinedInput-root _language__select_15g6v_35 _dark_15g6v_55   MuiInputBase-formControl"><div class="MuiSelect-root MuiSelect-select MuiSelect-selectMenu MuiSelect-outlined MuiInputBase-input MuiOutlinedInput-input" tabindex="0" role="button" aria-haspopup="listbox" aria-labelledby="language-select" id="language-select">Python3</div><input aria-hidden="true" tabindex="-1" class="MuiSelect-nativeInput" value="PYTH 3"><svg class="MuiSvgIcon-root MuiSelect-icon MuiSelect-iconOutlined" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 10l5 5 5-5z"></path></svg><fieldset aria-hidden="true" class="jss264 MuiOutlinedInput-notchedOutline" style="padding-left: 8px;"><legend class="jss265" style="width: 0.01px;"><span>​</span></legend></fieldset></div></div></div><ul class="_settings_1fs8l_2 _dark_1fs8l_71"><li><div class="_icon__container_1fs8l_16" title="Reset code"><i class="_reset__icon_1fs8l_41"></i></div></li><li><div class="_icon__container_1fs8l_16" title="Settings"><i class="_settings__icon_1fs8l_53"></i></div></li><li><div class="_icon__container_1fs8l_16" title="Go fullscreen"><i class="_fullscreen__icon_1fs8l_59 _dark_1fs8l_71"></i></div></li></ul></div><div class="_ideEditorWrapper_15g6v_175 _dark_15g6v_55  " style="height: calc(-290px + 100vh);"><div class="MuiBackdrop-root _ide-overlay__backdrop_15g6v_190" aria-hidden="true" style="opacity: 0; transition: opacity 195ms cubic-bezier(0.4, 0, 0.2, 1); visibility: hidden;"></div><div id="submit-ide-v2" class=" ace_editor ace-tomorrow-night ace_dark _ide__editor_15g6v_218" style="width: 500px; height: 100%; font-size: 14px;"><textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" aria-haspopup="false" aria-autocomplete="both" role="textbox" style="opacity: 0; font-size: 1px; height: 1px; width: 1px; top: 96px; left: 160px;"></textarea><div class="ace_gutter" aria-hidden="true" style="left: 0px; width: 41px;"><div class="ace_layer ace_gutter-layer ace_folding-enabled" style="height: 1e+06px; top: 16px; left: 0px; width: 41px;"><div class="ace_gutter-cell " aria-hidden="true" style="height: 16px; top: 0px;">1<span tabindex="0" style="display: none;"></span><span tabindex="0" style="display: none;"><span></span></span></div><div class="ace_gutter-cell " aria-hidden="false" style="height: 16px; top: 16px;">2<span tabindex="-1" style="display: inline-block; height: 16px;" class="ace_fold-widget ace_start ace_open" role="button" aria-label="Toggle code folding, rows 2 through 3" aria-expanded="true" title="Fold code"></span><span tabindex="0" style="display: none;"><span></span></span></div><div class="ace_gutter-cell " aria-hidden="true" style="height: 16px; top: 32px;">3<span tabindex="0" style="display: none;"></span><span tabindex="0" style="display: none;"><span></span></span></div><div class="ace_gutter-cell " aria-hidden="false" style="height: 16px; top: 48px;">4<span tabindex="-1" class="ace_fold-widget ace_start ace_open" role="button" aria-label="Toggle code folding, rows 4 through 5" aria-expanded="true" title="Fold code" style="display: inline-block; height: 16px;"></span><span tabindex="0" style="display: none;"><span></span></span></div><div class="ace_gutter-cell ace_gutter-active-line " aria-hidden="true" style="height: 16px; top: 64px;">5<span tabindex="0" style="display: none;"></span><span tabindex="0" style="display: none;"><span></span></span></div></div></div><div class="ace_scroller " style="line-height: 16px; left: 41px; right: 0px; bottom: 0px;"><div class="ace_content" style="top: 16px; left: 0px; width: 718px; height: 437px;"><div class="ace_layer ace_print-margin-layer"><div class="ace_print-margin" style="left: 620px; visibility: hidden;"></div></div><div class="ace_layer ace_marker-layer"><div class="ace_active-line" style="height: 16px; top: 64px; left: 0px; right: 0px;"></div><div class="ace_bracket ace_start ace_br15" style="height: 16px; width: 7.69727px; top: 64px; left: 111.762px;"></div><div class="ace_bracket ace_start ace_br15" style="height: 16px; width: 7.69727px; top: 64px; left: 73.2754px;"></div></div><div class="ace_layer ace_text-layer" style="height: 1e+06px; margin: 0px 4px; top: 0px; left: 0px;"><div class="ace_line_group" style="height: 16px; top: 0px;"><div class="ace_line" style="height: 16px;"><span class="ace_identifier">x</span><span class="ace_keyword ace_operator">=</span><span class="ace_support ace_function">int</span><span class="ace_paren ace_lparen">(</span><span class="ace_support ace_function">input</span><span class="ace_paren ace_lparen">(</span><span class="ace_paren ace_rparen">))</span></div></div><div class="ace_line_group" style="height: 16px; top: 16px;"><div class="ace_line" style="height: 16px;"><span class="ace_keyword">if</span> <span class="ace_identifier">x</span><span class="ace_keyword ace_operator">&gt;=</span><span class="ace_constant ace_numeric">12</span><span class="ace_punctuation">:</span></div></div><div class="ace_line_group" style="height: 16px; top: 32px;"><div class="ace_line" style="height: 16px;">    <span class="ace_keyword">print</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">"yes"</span><span class="ace_paren ace_rparen">)</span></div></div><div class="ace_line_group" style="height: 16px; top: 48px;"><div class="ace_line" style="height: 16px;"><span class="ace_keyword">else</span><span class="ace_punctuation">:</span></div></div><div class="ace_line_group" style="height: 16px; top: 64px;"><div class="ace_line" style="height: 16px;">    <span class="ace_keyword">print</span><span class="ace_paren ace_lparen">(</span><span class="ace_string">"no"</span><span class="ace_paren ace_rparen">)</span></div></div></div><div class="ace_layer ace_marker-layer"></div><div class="ace_layer ace_cursor-layer ace_hidden-cursors"><div class="ace_cursor" style="display: block; top: 64px; left: 119px; width: 8px; height: 16px; animation-duration: 1000ms;"></div></div></div></div><div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 22px; height: 405px; bottom: 0px;"><div class="ace_scrollbar-inner" style="width: 22px; height: 112px;">&nbsp;</div></div><div class="ace_scrollbar ace_scrollbar-h" style="display: none; height: 22px; left: 41px; right: 0px; width: 718px;"><div class="ace_scrollbar-inner" style="height: 22px; width: 718px;">&nbsp;</div></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;"><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;">הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה</div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; font-optical-sizing: inherit; font-size-adjust: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div></div></div></div></div><div class="_ide-execute__wrapper_r2w6z_20 "><div class="_ideExecuteWrapperRef_aot9r_2 _dark_aot9r_12 _simple-ideExecuteWrapperRef_aot9r_661"><div class="_ideExecuteWrapperComponents_aot9r_15  "><div class="_testcaseContainer_aot9r_331 _dark_aot9r_12"><div class="MuiPaper-root MuiAccordion-root _accordion_aot9r_334 Mui-expanded MuiPaper-elevation1"><div class="MuiButtonBase-root MuiAccordionSummary-root jss704 _accordion__summary_aot9r_339 Mui-expanded jss707" tabindex="0" role="button" aria-disabled="false" aria-expanded="true"><div class="MuiAccordionSummary-content jss705 Mui-expanded jss707"><span>Test against Custom Input</span></div><div class="MuiButtonBase-root MuiIconButton-root MuiAccordionSummary-expandIcon jss706 Mui-expanded jss707 MuiIconButton-edgeEnd" aria-disabled="false" aria-hidden="true"><span class="MuiIconButton-label"><svg class="MuiSvgIcon-root _expandMoreIcon_aot9r_657 _dark_aot9r_12" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M16.59 8.59L12 13.17 7.41 8.59 6 10l6 6 6-6z"></path></svg></span><span class="MuiTouchRipple-root"></span></div></div><div class="MuiCollapse-container MuiCollapse-entered" style="min-height: 0px;"><div class="MuiCollapse-wrapper"><div class="MuiCollapse-wrapperInner"><div role="region"><div class="MuiAccordionDetails-root _accordion__details_aot9r_345"><textarea placeholder="Your program will run with no input" class="_textarea_aot9r_350" style="margin: 10px 0px; resize: none; height: 100px; background: rgb(255, 255, 255); border: 1px solid rgb(232, 236, 244); border-radius: 4px;" disabled="">3
</textarea></div></div></div></div></div></div></div><div></div><div class="_runTab_aot9r_486 _dark_aot9r_12">Submission Queued...</div></div><div class="_runContainer_aot9r_49 _dark_aot9r_12  "><div class="_leftContainer_aot9r_79"></div><div class="_execute-btn-container_aot9r_139"><div class="_execute-btn-actions_aot9r_162"><button type="button" class="_compile__btn_aot9r_217" id="compile_btn" disabled=""><svg class="MuiSvgIcon-root _btn__icon_aot9r_235" focusable="false" viewBox="0 0 24 24" aria-hidden="true"><path d="M10 17l5-5-5-5v10z"></path></svg><span class="_btn__text_aot9r_240">Run</span></button><button type="button" id="submit_btn" class="_submit__btn_aot9r_256 _dark_aot9r_12" disabled="">Submit</button><button type="button" class="_next__problem-link_aot9r_216"><p class="_btn__text_aot9r_240">Next</p></button></div></div></div></div></div></div></div></div></div></div></div></div></div></div></div>
  <script type="text/javascript">
    if (window.location.pathname.split('/')[1] === 'pro') {
      const razorPay = document.createElement('script');
      razorPay.setAttribute('src', 'https://checkout.razorpay.com/v1/checkout.js');
      document.head.appendChild(razorPay);

      // const instamojo = document.createElement('script');
      // instamojo.setAttribute('src', 'https://js.instamojo.com/v1/checkout.js');
      // document.head.appendChild(instamojo);

    }
    const scriptElement = document.createElement('script');
    scriptElement.setAttribute('src',
            "/sites/all/modules/codechef_alerts/codechef_alerts.js?v=649c43b6894169b33b5557aa0374459d"
    );
    document.body.appendChild(scriptElement);
  </script>
  <script type="text/javascript" src="./cric12_files/cookies.js.download"></script>



<script type="text/javascript">
    window.CDN_URL = 'https://cdn.codechef.com';
    window.csrfToken = "e7d92652854a9f7e05ca9af67358d6064f3fee2589d13b763a885ec7b4e846e0";
    window.APPS_URL = 'https://www.codechef-apps.com';
    window.tawkPropertyId = '668d037a7a36f5aaec9634a5';
    window.widgetId = '1i2bdb6dt';
    try {
        window.codeChefUserData = {"status":"success","user":{"username":"safe_willow_38","uid":"4815680","profileImage":null,"profileImagePath":"https:\/\/cdn.codechef.com\/sites\/all\/themes\/abessive\/images\/user_default_thumb.jpg","oauth_buttons":null,"oauthData":null,"isUserTeam":false,"html_handle":"safe_willow_38","userRatingStar":0,"userRatingStarColor":"black","isAdmin":false,"isHYCAdmin":false,"isPremiumUser":false,"isVerifiedUser":true,"user_consented_privacy_policy_version":null,"user_consented_privacy_policy_on":null,"current_privacy_policy_version":"9721896","visitedContests":[],"rating":0,"userStarHtml":"","proDiscount":null,"theme":"dark","fullName":"CHAKRADAR REDDY D","pro_plan":null,"sale":{"isSaleOngoing":false,"saleDaysLeft":-91},"isUserPartOfAnyUserGroup":false,"userSelectedProgrammingLanguage":"PYTH 3","country":"India"},"time":1723522586,"ip":"2401:4900:675f:29b8:707a:30a8:c51:876d","adStrip":null};
    } catch (e) {
        window.codeChefUserData = {};
    }
</script>
<iframe allow="join-ad-interest-group" data-tagging-id="AW-16598187415" data-load-time="1723522584618" height="0" width="0" src="./cric12_files/16598187415.html" style="display: none; visibility: hidden;"></iframe><script src="./cric12_files/codechef_alerts.js.download"></script><div style="top: 0px; left: 0px; position: fixed; display: none; place-items: center; height: 100vh; width: 100vw; z-index: 10000; line-height: 1.5; font-size: 16px; backdrop-filter: blur(2px); background: rgba(0, 0, 0, 0.1); box-sizing: border-box;"></div><div class=" ace_editor ace_autocomplete ace_dark ace-tomorrow-night" style="font-size: 14px; top: 193.8px; left: 895.97px; height: 100px; display: none;"><textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" aria-haspopup="false" aria-autocomplete="both" role="textbox" aria-hidden="true" style="opacity: 0; font-size: 1px; top: 0px; left: -100px;"></textarea><div class="ace_gutter" aria-hidden="true" style="display: none; left: 0px;"><div class="ace_layer ace_gutter-layer ace_folding-enabled" style="height: 1e+06px;"></div></div><div class="ace_scroller " style="line-height: 20px; left: 0px; right: 0px; bottom: 0px;"><div class="ace_content" style="cursor: default; top: 0px; left: 0px; width: 298px; height: 140px;"><div class="ace_layer ace_print-margin-layer"><div class="ace_print-margin" style="left: 620px; visibility: hidden;"></div></div><div class="ace_layer ace_marker-layer"><div class="ace_active-line" style="height: 20px; top: 0px; left: 0px; right: 0px;"></div></div><div class="ace_layer ace_text-layer" role="listbox" aria-roledescription="Autocomplete suggestions" aria-label="Autocomplete suggestions" aria-activedescendant="suggest-aria-id:0" style="height: 1e+06px; margin: 0px 4px; top: 0px; left: 0px;"><div class="ace_line ace_selected" role="option" aria-roledescription="item" aria-label="None" aria-setsize="5" aria-posinset="1" aria-describedby="doc-tooltip" id="suggest-aria-id:0" aria-selected="true" style="height: 20px; top: 0px;"><span class="ace_completion-highlight">No</span><span class="ace_">ne</span><span class="ace_completion-spacer"> </span><span class="ace_completion-meta">keyword</span></div><div class="ace_line" style="height: 20px; top: 20px;"><span class="ace_completion-highlight">no</span><span class="ace_">nlocal</span><span class="ace_completion-spacer"> </span><span class="ace_completion-meta">keyword</span></div><div class="ace_line" role="option" aria-roledescription="item" aria-label="input" aria-setsize="21" aria-posinset="3" aria-describedby="doc-tooltip" style="height: 20px; top: 40px;"><span class="ace_completion-highlight">no</span><span class="ace_">t</span><span class="ace_completion-spacer"> </span><span class="ace_completion-meta">keyword</span></div><div class="ace_line" style="height: 20px; top: 60px;"><span class="ace_completion-highlight">No</span><span class="ace_">tImplemented</span><span class="ace_completion-spacer"> </span><span class="ace_completion-meta">keyword</span></div><div class="ace_line" style="height: 20px; top: 80px;"><span class="ace_">u</span><span class="ace_completion-highlight">n</span><span class="ace_">ic</span><span class="ace_completion-highlight">o</span><span class="ace_">de</span><span class="ace_completion-spacer"> </span><span class="ace_completion-meta">keyword</span></div></div><div class="ace_layer ace_marker-layer"></div><div class="ace_layer ace_cursor-layer ace_hidden-cursors" style="opacity: 0;"><div class="ace_cursor" style="display: block; top: 0px; left: 4px; width: 8px; height: 20px;"></div></div></div></div><div class="ace_scrollbar ace_scrollbar-v" style="width: 22px; height: 100px; bottom: 0px; display: none;"><div class="ace_scrollbar-inner" style="width: 22px; height: 100px;">&nbsp;</div></div><div class="ace_scrollbar ace_scrollbar-h" style="display: none; height: 22px; left: 0px; right: 0px; width: 298px;"><div class="ace_scrollbar-inner" style="height: 22px; width: 281px;">&nbsp;</div></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;"><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;">הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה</div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; font-optical-sizing: inherit; font-size-adjust: inherit; font-kerning: inherit; font-feature-settings: inherit; font-variation-settings: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div></div></div></body></html>