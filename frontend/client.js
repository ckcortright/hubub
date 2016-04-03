// var debug = false;

// if (typeof(client) === 'undefined') {
//   var client = {};
// }
// //client specific variables
// client.latPos = 0;
// client.longPos = 0;
// client.name = "";
// client.radius = 100;
// client.site = "0.0.0.0:8000/clamorchat/";
// client.facility = "local-chat"
// client.ws = new WebSocket('ws://' + client.site + client.facility + '?subscribe-broadcast&publish-broadcast');

// //Location functions
// client.pos = function(position){
//   client.latPos = position.coords.latitude;
//   client.longPos = position.coords.longitude;
//   if (debug === true) {
//     console.log(position.coords.latitude + " " + client.latPos);
//     console.log(position.coords.longitude + " " + client.longPos);
//   }
// };
// client.getLocation = function(){
//     if (navigator.geolocation) {
//         navigator.geolocation.getCurrentPosition(client.pos);
//         setTimeout(function debugit(){
//             if (debug === true){
//             console.log("lat= " + client.latPos + " long= " + client.longPos);
//           };
//         }, 1000);

//     } else {
//       //TODO: redirect somewhere to a page that says our service isn't avaliable.
//     }
// };

// //client websocket methods
// client.ws.opensocket = function() {
//   client.ws = new WebSocket('ws://' + client.site + client.facility + '=?subscribe-broadcast&publish-broadcast&echo');
// }
// client.ws.onopen = function() {
//     //Test websocket connection
//     if (debug === true) {
//       console.log("websocket connected");
//       setTimeout(send_message("Testing"), 4000);
//     }
// };
// client.ws.onmessage = function(e) {
//     console.log("Received: " + e.data);
// };
// client.ws.onerror = function(e) {
//     console.error(e);
// };
// client.ws.onclose = function(e) {
//     console.log("connection closed");
// };
// function send_message(msg) {
//     client.ws.send(msg);
// }

// //Get the client's current location
// client.getLocation();
