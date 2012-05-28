/**
 * @author timger <yishenggudou@gmail.com>
 * @timger http://weibo.com/zhanghaibo
 * @yishenggudou http://twitter.com/yishenggudou
 * Copyright (c) 2008-2011 timger - released under MIT License
 */
BucketModel = Backbone.Model.extend({
   
    defaults: {
      id: "",
      urlRoot: "",
      key: "",
      name: "",
      owner: "",
      ACL: "",
      file_count: "",
      size_count: "",
      create_date: ""
    },

    initialize: function() {
        this.set({cid:this.cid});
    } 
    
    });

BucketView = Backbone.View.extend({
    
    initialize:function(){
        
        this.el = $('tr[cid='+this.model.cid+']');
        this.template = $('#tmpl_buckets').html();
        // --- model event -------
        //this.model.bind('change', this.render);
        this.model.bind('destroy', this.remove);
        // -- end model event --------------
        this._events = {};
        //事件绑定为当前小局部的元素
        $('tr[cid='+this.model.cid+'] td.name').live("click",this.openbucket);
        $('tr[cid='+this.model.cid+'] td.save').live("click",this.save);
    },
    render :function(){
        //渲染数据
        var to_render = this.model.toJSON();
        to_render.cid=this.model.cid;
        var html = Mustache.to_html(this.template,to_render);
        if (!$(this.el).length){
        //元素不存在  追加到区域
            $('#buckets').append(html);
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
    
    //----------------- 事件应答函数  -------------------------
    openbucket : function (){
       //click the user name 
    },
    save : function(){
        alert("将要保存修改");
        var ACL = $(this.el).find('.ACL').text();
        this.model.set({ACL:ACL}) 
    } 

    //----------------- end  ----------------------------------
    });

BucketCollection  = Backbone.Collection.extend({
    model: BucketModel,
    initialize:function(){
        this.bind('add',this.addobj);
        this.bind('remove',this.removeobj);
        this.bind('reset',this.resetsets);
        //this.bind("change:title",this.changeobj);
    },
    // functions for response events ---
    resetsets:function(obj){
        console.log(["bucket Sets has add ",obj]);
        $('#buckets tr').remove();
        this.each(function(item){
            var bucketv = new BucketView({model:item});
            console.log(["render model",item]);
            bucketv.render();
        })
    },
    addobj:function(){
    },
    removeobj:function(){
    },
    changeobj:function(){
    }
});

