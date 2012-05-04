/**
* @author timger <yishenggudou@gmail.com>
* @timger http://weibo.com/zhanghaibo
* @yishenggudou http://twitter.com/yishenggudou
* Copyright (c) 2008-2011 timger - released under MIT License
*/
$.ajaxSetup({async:false})
function QSS_Init(){
/*setup ajax and baseurl
*see http://api.jquery.com/jQuery.ajax/
*后来放弃了,还是 服务器做一个中转比较靠谱
* 一下代理与服务器交互方法
* 需要兼容后台API所以没有用backbone.js的原生的fetch 和sync模式
*/
this.url_base = '/web/proxy/';
this.url_board = '/web/board/';
//this.url_qss = 'http://qss.qiyi.com/';
this.url_qss = 'http://qss.qiyi.domain/';
this.url_listbuckets = this.url_base;
this.headers = {'x-qss-accept':'json'};
$.ajaxSetup({
async:false,
dataType:'json',
//headers:this.headers,
});
this.accept = 'json'
};
QSS_Init.prototype.listbuckets = function(){
var url = this.url_listbuckets;
url.replace('//','/');
var tmp = {};
$.get(this.url_listbuckets,this.headers,function(data){
tmp = data;
},this.accept);
return tmp;
};
QSS_Init.prototype.getbucketinfo = function(bucketname){
var url = this.url_base+'/'+bucketname+'/';
url.replace('//','/');
var tmp = {};
$.get(url,_.extend({acl:''},this.headers),function(data){
tmp=data;
},this.accept);
return tmp;
};
QSS_Init.prototype.listfiles = function(bucketname,start,end,step){
var url = this.url_base+'/'+bucketname+'/';
url.replace('//','/');
var tmp={};
$.get(url,this.headers,function(data){
tmp=data;
},this.accept)
return tmp;
}
QSS_Init.prototype.getfileinfo = function(filename){
var url = this.url_base+'/'+filename+'/';
url.replace('//','/');
var tmp = {};
$.get(url,_.extend({acl:''},this.headers),function(data){
tmp=data
},this.accept)
return tmp
}
QSS_Init.prototype.Delete = function(key){
var key = key.replace(/^\//,'');
var url = this.url_board;
var uri = this.url_qss+key;
var tmp = {};
var headers = _.clone(this.headers);
url = url.replace('//','/');
var payload = { method:'DELETE',
uri:uri,
headers:headers
};
$.post(url,{payload:JSON.stringify(payload)},function(data){
tmp=data
},this.accept);
console.log(['request a delete',payload,'result',tmp]);
return tmp
}
QSS_Init.prototype.Post = function(key){
var key = key.replace(/^\//,'');
var url = this.url_board;
var uri = this.url_qss+key;
var tmp = {};
var headers = _.clone(this.headers);
url = url.replace('//','/');
var payload = { method:'POST',
uri:uri,
headers:headers
};
$.post(url,{payload:JSON.stringify(payload)},function(data){
tmp=data
},this.accept)
console.log(['request a post',payload,'result',tmp]);
return tmp
}
QSS_Init.prototype.Put = function(key){
var key = key.replace(/^\//,'');
var url = this.url_board;
var uri = this.url_qss+key;
var tmp = {};
var headers = _.clone(this.headers);
url = url.replace('//','/');
var payload = { method:'PUT',
uri:uri,
headers:headers
};
$.post(url,{payload:JSON.stringify(payload)},function(data){
tmp=data;
},this.accept)
console.log(['request a put',payload,'result',tmp]);
return tmp
}
QSS_Init.prototype.Get = function(key){
var key = key.replace(/^\//,'');
var url = this.url_board;
var uri = this.url_qss+key;
var tmp = {};
var headers = _.clone(this.headers);
url = url.replace('//','/');
var payload = { method:'GET',
uri:uri,
headers:headers
};
$.post(url,{payload:JSON.stringify(payload)},function(data){
tmp=data
},this.accept)
console.log(['request a get',payload,'result',tmp]);
return tmp
}
QSS_Init.prototype.Head = function(key){
var key = key.replace(/^\//,'');
var url = this.url_board;
var uri = this.url_qss+key;
var tmp = {};
var headers = _.clone(this.headers);
url = url.replace('//','/');
var payload = { method:'HEAD',
uri:uri,
headers:headers
};
$.post(url,{payload:JSON.stringify(payload)},function(data){
tmp=data
},this.accept)
console.log(['request a head',payload,'result',tmp]);
return tmp
} 
