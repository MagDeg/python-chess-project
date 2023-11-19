"use strict";(self["webpackChunk_jupyterlab_application_top"]=self["webpackChunk_jupyterlab_application_top"]||[]).push([[4633],{44633:(t,e,i)=>{i.r(e);i.d(e,{diagram:()=>D});var n=i(85582);var s=i(34596);var r=i(27484);var a=i.n(r);var l=i(17967);var c=i(27856);var o=i.n(c);var h=function(){var t=function(t,e,i,n){for(i=i||{},n=t.length;n--;i[t[n]]=e);return i},e=[1,3],i=[1,4],n=[1,5],s=[1,6],r=[1,10,12,14,16,18,19,20,21,22],a=[2,4],l=[1,5,10,12,14,16,18,19,20,21,22],c=[20,21,22],o=[2,7],h=[1,12],u=[1,13],y=[1,14],p=[1,15],f=[1,16],d=[1,17];var g={trace:function t(){},yy:{},symbols_:{error:2,start:3,eol:4,PIE:5,document:6,showData:7,line:8,statement:9,txt:10,value:11,title:12,title_value:13,acc_title:14,acc_title_value:15,acc_descr:16,acc_descr_value:17,acc_descr_multiline_value:18,section:19,NEWLINE:20,";":21,EOF:22,$accept:0,$end:1},terminals_:{2:"error",5:"PIE",7:"showData",10:"txt",11:"value",12:"title",13:"title_value",14:"acc_title",15:"acc_title_value",16:"acc_descr",17:"acc_descr_value",18:"acc_descr_multiline_value",19:"section",20:"NEWLINE",21:";",22:"EOF"},productions_:[0,[3,2],[3,2],[3,3],[6,0],[6,2],[8,2],[9,0],[9,2],[9,2],[9,2],[9,2],[9,1],[9,1],[4,1],[4,1],[4,1]],performAction:function t(e,i,n,s,r,a,l){var c=a.length-1;switch(r){case 3:s.setShowData(true);break;case 6:this.$=a[c-1];break;case 8:s.addSection(a[c-1],s.cleanupValue(a[c]));break;case 9:this.$=a[c].trim();s.setDiagramTitle(this.$);break;case 10:this.$=a[c].trim();s.setAccTitle(this.$);break;case 11:case 12:this.$=a[c].trim();s.setAccDescription(this.$);break;case 13:s.addSection(a[c].substr(8));this.$=a[c].substr(8);break}},table:[{3:1,4:2,5:e,20:i,21:n,22:s},{1:[3]},{3:7,4:2,5:e,20:i,21:n,22:s},t(r,a,{6:8,7:[1,9]}),t(l,[2,14]),t(l,[2,15]),t(l,[2,16]),{1:[2,1]},t(c,o,{8:10,9:11,1:[2,2],10:h,12:u,14:y,16:p,18:f,19:d}),t(r,a,{6:18}),t(r,[2,5]),{4:19,20:i,21:n,22:s},{11:[1,20]},{13:[1,21]},{15:[1,22]},{17:[1,23]},t(c,[2,12]),t(c,[2,13]),t(c,o,{8:10,9:11,1:[2,3],10:h,12:u,14:y,16:p,18:f,19:d}),t(r,[2,6]),t(c,[2,8]),t(c,[2,9]),t(c,[2,10]),t(c,[2,11])],defaultActions:{7:[2,1]},parseError:function t(e,i){if(i.recoverable){this.trace(e)}else{var n=new Error(e);n.hash=i;throw n}},parse:function t(e){var i=this,n=[0],s=[],r=[null],a=[],l=this.table,c="",o=0,h=0,u=2,y=1;var p=a.slice.call(arguments,1);var f=Object.create(this.lexer);var d={yy:{}};for(var g in this.yy){if(Object.prototype.hasOwnProperty.call(this.yy,g)){d.yy[g]=this.yy[g]}}f.setInput(e,d.yy);d.yy.lexer=f;d.yy.parser=this;if(typeof f.yylloc=="undefined"){f.yylloc={}}var _=f.yylloc;a.push(_);var m=f.options&&f.options.ranges;if(typeof d.yy.parseError==="function"){this.parseError=d.yy.parseError}else{this.parseError=Object.getPrototypeOf(this).parseError}function v(){var t;t=s.pop()||f.lex()||y;if(typeof t!=="number"){if(t instanceof Array){s=t;t=s.pop()}t=i.symbols_[t]||t}return t}var b,k,x,S,w={},$,E,A,T;while(true){k=n[n.length-1];if(this.defaultActions[k]){x=this.defaultActions[k]}else{if(b===null||typeof b=="undefined"){b=v()}x=l[k]&&l[k][b]}if(typeof x==="undefined"||!x.length||!x[0]){var I="";T=[];for($ in l[k]){if(this.terminals_[$]&&$>u){T.push("'"+this.terminals_[$]+"'")}}if(f.showPosition){I="Parse error on line "+(o+1)+":\n"+f.showPosition()+"\nExpecting "+T.join(", ")+", got '"+(this.terminals_[b]||b)+"'"}else{I="Parse error on line "+(o+1)+": Unexpected "+(b==y?"end of input":"'"+(this.terminals_[b]||b)+"'")}this.parseError(I,{text:f.match,token:this.terminals_[b]||b,line:f.yylineno,loc:_,expected:T})}if(x[0]instanceof Array&&x.length>1){throw new Error("Parse Error: multiple actions possible at state: "+k+", token: "+b)}switch(x[0]){case 1:n.push(b);r.push(f.yytext);a.push(f.yylloc);n.push(x[1]);b=null;{h=f.yyleng;c=f.yytext;o=f.yylineno;_=f.yylloc}break;case 2:E=this.productions_[x[1]][1];w.$=r[r.length-E];w._$={first_line:a[a.length-(E||1)].first_line,last_line:a[a.length-1].last_line,first_column:a[a.length-(E||1)].first_column,last_column:a[a.length-1].last_column};if(m){w._$.range=[a[a.length-(E||1)].range[0],a[a.length-1].range[1]]}S=this.performAction.apply(w,[c,h,o,d.yy,x[1],r,a].concat(p));if(typeof S!=="undefined"){return S}if(E){n=n.slice(0,-1*E*2);r=r.slice(0,-1*E);a=a.slice(0,-1*E)}n.push(this.productions_[x[1]][0]);r.push(w.$);a.push(w._$);A=l[n[n.length-2]][n[n.length-1]];n.push(A);break;case 3:return true}}return true}};var _=function(){var t={EOF:1,parseError:function t(e,i){if(this.yy.parser){this.yy.parser.parseError(e,i)}else{throw new Error(e)}},setInput:function(t,e){this.yy=e||this.yy||{};this._input=t;this._more=this._backtrack=this.done=false;this.yylineno=this.yyleng=0;this.yytext=this.matched=this.match="";this.conditionStack=["INITIAL"];this.yylloc={first_line:1,first_column:0,last_line:1,last_column:0};if(this.options.ranges){this.yylloc.range=[0,0]}this.offset=0;return this},input:function(){var t=this._input[0];this.yytext+=t;this.yyleng++;this.offset++;this.match+=t;this.matched+=t;var e=t.match(/(?:\r\n?|\n).*/g);if(e){this.yylineno++;this.yylloc.last_line++}else{this.yylloc.last_column++}if(this.options.ranges){this.yylloc.range[1]++}this._input=this._input.slice(1);return t},unput:function(t){var e=t.length;var i=t.split(/(?:\r\n?|\n)/g);this._input=t+this._input;this.yytext=this.yytext.substr(0,this.yytext.length-e);this.offset-=e;var n=this.match.split(/(?:\r\n?|\n)/g);this.match=this.match.substr(0,this.match.length-1);this.matched=this.matched.substr(0,this.matched.length-1);if(i.length-1){this.yylineno-=i.length-1}var s=this.yylloc.range;this.yylloc={first_line:this.yylloc.first_line,last_line:this.yylineno+1,first_column:this.yylloc.first_column,last_column:i?(i.length===n.length?this.yylloc.first_column:0)+n[n.length-i.length].length-i[0].length:this.yylloc.first_column-e};if(this.options.ranges){this.yylloc.range=[s[0],s[0]+this.yyleng-e]}this.yyleng=this.yytext.length;return this},more:function(){this._more=true;return this},reject:function(){if(this.options.backtrack_lexer){this._backtrack=true}else{return this.parseError("Lexical error on line "+(this.yylineno+1)+". You can only invoke reject() in the lexer when the lexer is of the backtracking persuasion (options.backtrack_lexer = true).\n"+this.showPosition(),{text:"",token:null,line:this.yylineno})}return this},less:function(t){this.unput(this.match.slice(t))},pastInput:function(){var t=this.matched.substr(0,this.matched.length-this.match.length);return(t.length>20?"...":"")+t.substr(-20).replace(/\n/g,"")},upcomingInput:function(){var t=this.match;if(t.length<20){t+=this._input.substr(0,20-t.length)}return(t.substr(0,20)+(t.length>20?"...":"")).replace(/\n/g,"")},showPosition:function(){var t=this.pastInput();var e=new Array(t.length+1).join("-");return t+this.upcomingInput()+"\n"+e+"^"},test_match:function(t,e){var i,n,s;if(this.options.backtrack_lexer){s={yylineno:this.yylineno,yylloc:{first_line:this.yylloc.first_line,last_line:this.last_line,first_column:this.yylloc.first_column,last_column:this.yylloc.last_column},yytext:this.yytext,match:this.match,matches:this.matches,matched:this.matched,yyleng:this.yyleng,offset:this.offset,_more:this._more,_input:this._input,yy:this.yy,conditionStack:this.conditionStack.slice(0),done:this.done};if(this.options.ranges){s.yylloc.range=this.yylloc.range.slice(0)}}n=t[0].match(/(?:\r\n?|\n).*/g);if(n){this.yylineno+=n.length}this.yylloc={first_line:this.yylloc.last_line,last_line:this.yylineno+1,first_column:this.yylloc.last_column,last_column:n?n[n.length-1].length-n[n.length-1].match(/\r?\n?/)[0].length:this.yylloc.last_column+t[0].length};this.yytext+=t[0];this.match+=t[0];this.matches=t;this.yyleng=this.yytext.length;if(this.options.ranges){this.yylloc.range=[this.offset,this.offset+=this.yyleng]}this._more=false;this._backtrack=false;this._input=this._input.slice(t[0].length);this.matched+=t[0];i=this.performAction.call(this,this.yy,this,e,this.conditionStack[this.conditionStack.length-1]);if(this.done&&this._input){this.done=false}if(i){return i}else if(this._backtrack){for(var r in s){this[r]=s[r]}return false}return false},next:function(){if(this.done){return this.EOF}if(!this._input){this.done=true}var t,e,i,n;if(!this._more){this.yytext="";this.match=""}var s=this._currentRules();for(var r=0;r<s.length;r++){i=this._input.match(this.rules[s[r]]);if(i&&(!e||i[0].length>e[0].length)){e=i;n=r;if(this.options.backtrack_lexer){t=this.test_match(i,s[r]);if(t!==false){return t}else if(this._backtrack){e=false;continue}else{return false}}else if(!this.options.flex){break}}}if(e){t=this.test_match(e,s[n]);if(t!==false){return t}return false}if(this._input===""){return this.EOF}else{return this.parseError("Lexical error on line "+(this.yylineno+1)+". Unrecognized text.\n"+this.showPosition(),{text:"",token:null,line:this.yylineno})}},lex:function t(){var e=this.next();if(e){return e}else{return this.lex()}},begin:function t(e){this.conditionStack.push(e)},popState:function t(){var e=this.conditionStack.length-1;if(e>0){return this.conditionStack.pop()}else{return this.conditionStack[0]}},_currentRules:function t(){if(this.conditionStack.length&&this.conditionStack[this.conditionStack.length-1]){return this.conditions[this.conditionStack[this.conditionStack.length-1]].rules}else{return this.conditions["INITIAL"].rules}},topState:function t(e){e=this.conditionStack.length-1-Math.abs(e||0);if(e>=0){return this.conditionStack[e]}else{return"INITIAL"}},pushState:function t(e){this.begin(e)},stateStackSize:function t(){return this.conditionStack.length},options:{"case-insensitive":true},performAction:function t(e,i,n,s){switch(n){case 0:break;case 1:break;case 2:return 20;case 3:break;case 4:break;case 5:this.begin("title");return 12;case 6:this.popState();return"title_value";case 7:this.begin("acc_title");return 14;case 8:this.popState();return"acc_title_value";case 9:this.begin("acc_descr");return 16;case 10:this.popState();return"acc_descr_value";case 11:this.begin("acc_descr_multiline");break;case 12:this.popState();break;case 13:return"acc_descr_multiline_value";case 14:this.begin("string");break;case 15:this.popState();break;case 16:return"txt";case 17:return 5;case 18:return 7;case 19:return"value";case 20:return 22}},rules:[/^(?:%%(?!\{)[^\n]*)/i,/^(?:[^\}]%%[^\n]*)/i,/^(?:[\n\r]+)/i,/^(?:%%[^\n]*)/i,/^(?:[\s]+)/i,/^(?:title\b)/i,/^(?:(?!\n||)*[^\n]*)/i,/^(?:accTitle\s*:\s*)/i,/^(?:(?!\n||)*[^\n]*)/i,/^(?:accDescr\s*:\s*)/i,/^(?:(?!\n||)*[^\n]*)/i,/^(?:accDescr\s*\{\s*)/i,/^(?:[\}])/i,/^(?:[^\}]*)/i,/^(?:["])/i,/^(?:["])/i,/^(?:[^"]*)/i,/^(?:pie\b)/i,/^(?:showData\b)/i,/^(?::[\s]*[\d]+(?:\.[\d]+)?)/i,/^(?:$)/i],conditions:{acc_descr_multiline:{rules:[12,13],inclusive:false},acc_descr:{rules:[10],inclusive:false},acc_title:{rules:[8],inclusive:false},title:{rules:[6],inclusive:false},string:{rules:[15,16],inclusive:false},INITIAL:{rules:[0,1,2,3,4,5,7,9,11,14,17,18,19,20],inclusive:true}}};return t}();g.lexer=_;function m(){this.yy={}}m.prototype=g;g.Parser=m;return new m}();h.parser=h;const u=h;const y=n.A.pie;const p={sections:{},showData:false,config:y};let f=p.sections;let d=p.showData;const g=structuredClone(y);const _=()=>structuredClone(g);const m=()=>{f=structuredClone(p.sections);d=p.showData;(0,n.t)()};const v=(t,e)=>{t=(0,n.d)(t,(0,n.c)());if(f[t]===void 0){f[t]=e;n.l.debug(`added new section: ${t}, with value: ${e}`)}};const b=()=>f;const k=t=>{if(t.substring(0,1)===":"){t=t.substring(1).trim()}return Number(t.trim())};const x=t=>{d=t};const S=()=>d;const w={getConfig:_,clear:m,setDiagramTitle:n.q,getDiagramTitle:n.r,setAccTitle:n.s,getAccTitle:n.g,setAccDescription:n.b,getAccDescription:n.a,addSection:v,getSections:b,cleanupValue:k,setShowData:x,getShowData:S};const $=t=>`\n  .pieCircle{\n    stroke: ${t.pieStrokeColor};\n    stroke-width : ${t.pieStrokeWidth};\n    opacity : ${t.pieOpacity};\n  }\n  .pieOuterCircle{\n    stroke: ${t.pieOuterStrokeColor};\n    stroke-width: ${t.pieOuterStrokeWidth};\n    fill: none;\n  }\n  .pieTitleText {\n    text-anchor: middle;\n    font-size: ${t.pieTitleTextSize};\n    fill: ${t.pieTitleTextColor};\n    font-family: ${t.fontFamily};\n  }\n  .slice {\n    font-family: ${t.fontFamily};\n    fill: ${t.pieSectionTextColor};\n    font-size:${t.pieSectionTextSize};\n    // fill: white;\n  }\n  .legend text {\n    fill: ${t.pieLegendTextColor};\n    font-family: ${t.fontFamily};\n    font-size: ${t.pieLegendTextSize};\n  }\n`;const E=$;const A=t=>{const e=Object.entries(t).map((t=>({label:t[0],value:t[1]}))).sort(((t,e)=>e.value-t.value));const i=(0,s.ve8)().value((t=>t.value));return i(e)};const T=(t,e,i,r)=>{var a,l;n.l.debug("rendering pie chart\n"+t);const c=r.db;const o=(0,n.c)();const h=(0,n.B)(c.getConfig(),o.pie);const u=450;const y=((l=(a=document.getElementById(e))==null?void 0:a.parentElement)==null?void 0:l.offsetWidth)??h.useWidth;const p=(0,n.z)(e);p.attr("viewBox",`0 0 ${y} ${u}`);(0,n.i)(p,u,y,h.useMaxWidth);const f=40;const d=18;const g=4;const _=p.append("g");_.attr("transform","translate("+y/2+","+u/2+")");const{themeVariables:m}=o;let[v]=(0,n.C)(m.pieOuterStrokeWidth);v??(v=2);const b=h.textPosition;const k=Math.min(y,u)/2-f;const x=(0,s.Nb1)().innerRadius(0).outerRadius(k);const S=(0,s.Nb1)().innerRadius(k*b).outerRadius(k*b);_.append("circle").attr("cx",0).attr("cy",0).attr("r",k+v/2).attr("class","pieOuterCircle");const w=c.getSections();const $=A(w);const E=[m.pie1,m.pie2,m.pie3,m.pie4,m.pie5,m.pie6,m.pie7,m.pie8,m.pie9,m.pie10,m.pie11,m.pie12];const T=(0,s.PKp)(E);_.selectAll("mySlices").data($).enter().append("path").attr("d",x).attr("fill",(t=>T(t.data.label))).attr("class","pieCircle");let I=0;Object.keys(w).forEach((t=>{I+=w[t]}));_.selectAll("mySlices").data($).enter().append("text").text((t=>(t.data.value/I*100).toFixed(0)+"%")).attr("transform",(t=>"translate("+S.centroid(t)+")")).style("text-anchor","middle").attr("class","slice");_.append("text").text(c.getDiagramTitle()).attr("x",0).attr("y",-(u-50)/2).attr("class","pieTitleText");const D=_.selectAll(".legend").data(T.domain()).enter().append("g").attr("class","legend").attr("transform",((t,e)=>{const i=d+g;const n=i*T.domain().length/2;const s=12*d;const r=e*i-n;return"translate("+s+","+r+")"}));D.append("rect").attr("width",d).attr("height",d).style("fill",T).style("stroke",T);D.data($).append("text").attr("x",d+g).attr("y",d-g).text((t=>{const{label:e,value:i}=t.data;if(c.getShowData()){return`${e} [${i}]`}return e}))};const I={draw:T};const D={parser:u,db:w,renderer:I,styles:E}}}]);