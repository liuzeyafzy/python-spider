var webPage = require('webpage');
var page = webPage.create();

page.open('https://www.btc123.com/market?symbol=huobibtcusdt',/*'http://phantomjs.org',*/ function (status) {
  var cookies = page.cookies;
  console.log(status)
  
  console.log('Listing cookies:');
  for(var i in cookies) {
    console.log(cookies[i].name + '=' + cookies[i].value);
  }
  
  // var script1 = "return GLOBAL_VAR.KLineData"
  // page.evaluateJavaScript(script1);
  
  // 这里尝试过直接在里面调用console.log()，但是没法在命令行中显示出来。//想想，这是为什么。
  // 现在改成return之后再处理就好了。
  var rtnValue = page.evaluate(function(){
    // console.log(GLOBAL_VAR.KLineData)
    // console.log("GLOBAL_VAR.KLineData")
    return window.GLOBAL_VAR.KLineData
  });
  console.log(rtnValue)

  // page.onResourceRequested = function (request) {
  //   console.log('Request ' + JSON.stringify(request, undefined, 4));
  // };

  // page.evaluate(function() {
  //   // $("button").click();
    
  // });
  phantom.exit();
});
