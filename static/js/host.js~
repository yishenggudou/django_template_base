/**
 * @author timger <yishenggudou@gmail.com>
 * @timger http://weibo.com/zhanghaibo
 * @yishenggudou http://twitter.com/yishenggudou
 * Copyright (c) 2008-2011 timger - released under MIT License
 */
PathModel = Backbone.Model.extend({
                    urlRoot: '/paths',
                    });
PathCollection  = Backbone.Collection.extend({
    model: PathModel,
    })

HostModel = Backbone.Model.extend({
   
    defaults: {
      host:"",
      data:[],
      urlRoot: "",
      used: "",        //已经使用
      ip: "",
      free_space: "",  //实际可用
      avaiable: "",    //可用
      recyclebin: "",  //回收站
      maxsize: "",     //总的分配空间
    },

    initialize: function() {
        this.set({cid:this.cid});
        var data = this.get('data'),paths = [];
        console.log(['data-----------------------',data])
        this.set({id:data.id});
        for (i in data.paths){
            var tmp = {},item = data.paths[i];
            tmp.free_space = parseFloat(parseInt(item.free_space)/(1024*1024*1024)).toFixed(2)+'GB';
            tmp.used = parseFloat(parseInt(item.used)/(1024*1024*1024)).toFixed(2)+'GB';
            tmp.available = parseFloat(parseInt(item.available)/(1024*1024*1024)).toFixed(2)+'GB';
            tmp.maxsize = parseFloat(parseInt(item.maxsize)/(1024*1024*1024)).toFixed(2)+'GB';
            tmp.recyclebin = parseFloat(parseInt(item.recyclebin)/(1024*1024*1024)).toFixed(2)+'GB';
            tmp.available_alert = parseInt(item.free_space)/parseInt(item.maxsize) < 0.2
            tmp.free_space_alert = parseInt(item.free_space) <= parseInt(item.available)
            tmp.need_delete = parseInt(item.free_space)/parseInt(item.maxsize) <= 0.3 
            tmp.path = item.path; 
            tmp.usebar = parseInt(item.used)*100/parseInt(item.maxsize);
            tmp.use_tash_bar = (parseInt(item.used)+parseInt(item.recyclebin))*100/parseInt(item.maxsize);
            tmp.is_online = (item.status == 0);
            tmp.is_offline = (item.status == 2);
            tmp.is_bug = (item.status == 1);
            tmp.is_recover = (item.status == 3);
            tmp.id = item.id;
            console.log(['path',tmp,item])
            paths.push(_.clone(tmp));
        };
        data.paths = paths;
        data.is_online = Boolean(data.status == 0);
        data.is_offline = Boolean(data.status==2);
        data.is_bug = Boolean(data.status==1);
        console.log(['data',data])
        this.set({data:data});
        this.set({is_offline:data.is_offline});
        this.set({is_online:data.is_online});
        this.set({is_bug:data.is_bug});
        
        
        
        //this.set({total:parseInt(this.get('used'))+parseInt(this.get('free_space'))+parseInt(this.get('avaiable'))})
    } 
    
    });

HostView = Backbone.View.extend({
   
    initialize:function(){
        
        var that = this;
        this.template=$('#tmpl_hosts').html();
        this.el = $('tr[cid='+this.model.cid+']');
        
        // --- model event -------
        //this.model.bind('change', this.render);
        this.model.bind('destroy', this.remove);
        // -- end model event --------------
        this._events = {};
        
        //事件绑定为当前小局部的元素
        //$('tr[cid='+this.model.cid+'] td.name').live("click",this.openhost);
        //$('tr[cid='+this.model.cid+'] td.save').live('click',this.save);

        $('tr[cid='+this.model.cid+'] table tbody td[dis=switch]').live("click",this.switchonline);
        $('tr[cid='+this.model.cid+'] table tbody td[dis=save]').live("click",this.updatedata);
    },
    render :function(){
        //渲染数据
        var to_render = this.model.toJSON();
        to_render.cid=this.model.cid;
        var html = Mustache.to_html(this.template,to_render);
        if (!$(this.el).length){
        //元素不存在  追加到区域
            $('#hosts').append(html);
        }else{
        //元素存在
            $(this.el).replaceWith(html);
        };
        //$(this.el).live("click",function(){})
    },
    remove: function (){
        if (!$(this.el).length){
        //元素不存在  追加到区域
            
        }else{
        //元素存在
            $(this.el).destroy();
        }
    },
    toggleViewed:function(){
        //切换试图现实还是隐藏
        if ($(this.el).length){
            if ( $(this.el).is(":visible")){
                $(this.el).hide();
            }else{
                $(this.el).show();
            }
        }
    },
    
    events : this._events,
    //----------------- 事件应答函数  -------------------------
    //
    updatedata : function(event){
        console.log(['start update the data']) 
    
        },
    switchonline:function(event){
        var path = $(event.target).parent().attr('path'),
        todo = $(event.target).attr('todo'),
        t = $(event.target).parent(),
        hostid = $(event.target).parent().attr('hostid');
        if (todo == 'offline') {
            alert("将要下线该存储空间");
            a =  new PathModel({
                    id : $(t).attr('pid'),
                    status:2
            });
            a.save({},{success :function(model,response){
                                console.log(['save to file success'])
                                alert("下线成功");
                                Backbone.history.loadUrl('#hosts');
                                //location.hash='#hosts'
                            },
                    error   :function(model,response){
                                alert("下线失败");
                                Backbone.history.loadUrl('#hosts');
                                //location.hash='#hosts';
                             }  
            });
                        
        }else if (todo == 'online'){
            alert("将要上线该存储空间"); 
            a =  new PathModel({
                    id : $(t).attr('pid'),
                    status:0
            });
             a.save({},{success :function(model,response){
                                if (response.status == 0){
                                     alert("上线成功");
                                     console.log(['success online',response])
                                     Backbone.history.loadUrl('#hosts');
                                }
                                else{
                                     alert("操作失败");
                                     return false;
                                }
                                //location.hash='#hosts';
                            },
                        error   :function(model,response){
                                alert("上线失败");
                                Backbone.history.loadUrl('#hosts');
                                //location.hash='#hosts'
                             }  
            });

        
        }
    },
    openhost : function (){
       //click the host name 
    },
    save : function(){
    } 

    //----------------- end  ----------------------------------
    });

HostCollection  = Backbone.Collection.extend({
    model: HostModel,
    initialize:function(){
        this.bind('add',this.addobj);
        this.bind('reset',this.resetsets);
        this.bind('remove',this.removeobj);
        //this.bind("change:title",this.changeobj);
    },
    // functions for response events ---
    resetsets:function(obj){
        console.log(["host Sets has add ",obj]);
        $('#hosts tr').remove();
        this.each(function(item){
            console.log(["render model",item]);
            var hostv = new HostView({model:item});
            hostv.render();
            $('#hosts td,#host_head td')
                          .css('padding','1px 1px 1px 1px')
                          .height('auto')
                          .css('margin','0px 0px 0px 0px')
                          .css('width','200px')
                          .css("min-width","100px")
        $('tr.host  td[dis=save]').attr('title','点击可以修改数值');
        })
    },
    addobj:function(){
    },
    removeobj:function(){

    },
    changeobj:function(){
    }
});

