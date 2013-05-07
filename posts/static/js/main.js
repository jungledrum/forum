$(function(){
  $("#subject_btn").click(function(){
    title = $("input[name='title']");
    content = $("textarea[name='content']");
    username = $('#username');
    csrf_token = $('input[name="csrfmiddlewaretoken"]')    
    $.post(
      "/posts/create/", 
      { title: title.val(), content: content.val(), csrfmiddlewaretoken: csrf_token.val() },
      function(data){
        $("table[name='posts']").append('<tr><td><a href="/posts/'+data+'/">'+title.val()+'</a></td><td>'+username.text()+'</td><td><a href="/posts/'+data+'/destroy/">删除</a></td></tr>');
        title.val("");
        content.val("");
      }
    );

  });

  $("#comment_btn").click(function(){
    content = $("textarea[name='content']");
    username = $('#username');
    post_id = $('input[name="post_id"]').val()
    csrf_token = $('input[name="csrfmiddlewaretoken"]');
    $.post(
      $('form[name="comment_form"]').attr('action'), 
      { content: content.val(), csrfmiddlewaretoken: csrf_token.val() },
      function(data){
        $("table[name='comments']").append('<tr><td>'+username.text()+'</td><td>'+content.val()+'</td><td><a href="/posts/'+post_id+'/comments/'+data+'/destroy/">删除</a></td></tr>');
        content.val("");
      }
    );
  });
})