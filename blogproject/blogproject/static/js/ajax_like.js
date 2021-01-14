function addOrRemoveLike(blogId) {
    $.ajax({
      type: "POST",
      url: "{% url 'add_or_remove_like_ajax' %}",
      data:{
        blog_id: blogId,
        csrfmiddlewaretoken: "{{csrf_token}}"
      },
      success: function (data) {
            alert('Everything worked with data: ' + data)

      }
    });
};