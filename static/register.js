/**
 * Created by 徐光宇 on 2018/8/31.
 */
window.onload = function () {
    var mySubmit = document.getElementById("mySubmit");
    mySubmit.onclick = function () {
        var title = document.getElementsByName("title")[0];
        var author = document.getElementsByName("author")[0];
        var publishDate = document.getElementsByName("publishDate")[0];
        var publish = document.getElementsByName("publish")[0];
        var price = document.getElementsByName("price")[0];
        console.log(title.value);
        if(title.value && author.value && publishDate.value && price.value && publish.value){
            document.getElementsByTagName("form")[0].submit();
            return true;
        }else{
            alert("内容不能为空");
            return  false;
        }
    }
};