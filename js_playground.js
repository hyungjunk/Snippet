var qr = $("#qrcode");
var callback = function do_print() {
    console.log("doc ready");
};
observer = new MutationObserver(callback);
observer.observe(qr[0], {attributes:true, childList:true, subtree:true});
