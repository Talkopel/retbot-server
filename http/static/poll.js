(function(){ 
	// var clickPromise = new Promise(function(resolve) {
	// 	document.body.addEventListener("click", function() {
	// 		resolve(["127.0.0.1", "dirty.txt", "1235432", "100"])
	// 	});
	// }).then(function(v) {
	// 	gotAlert(v[0], v[1], v[2], v[3]);
	// });

// for real code, uncomment the below.
	setInterval(function() {
			// code expects the following format for the JSON
			// ["127.0.0.1", "dirty.txt", "1235432", "100"] 
		fetch("/alert").then(function(res){ return res.json(); }).then(function(v){
			gotAlert(v[0], v[1], v[2], v[3]);
		});
	}, 200);
})();

function gotAlert(ip, file, time, uid) {
	document.querySelector("#matrix_effect").style.display = "none";
	document.querySelector(".output-console").style.display = "none";
	document.querySelector(".bars-and-stuff").style.display = "none";
	document.body.style.backgroundColor = "#990000";
	var flag = true;
	var interval = setInterval(function() {
		document.body.style.backgroundColor = flag? "#AA0000" : "#990000";
		flag = !flag;
	}, 400);
	window.danger = true;
	var close = function() {
		basicModal.close();
		window.danger = false;
		clearInterval(interval);
		document.querySelector("#matrix_effect").style.display = "";
		document.querySelector(".output-console").style.display = "";
		document.querySelector(".bars-and-stuff").style.display = "";
		document.body.style.backgroundColor = "";

	}
	basicModal.show({
	    body: `<img src='warning.png' style='width: 100px'><img src='warning.png' style='width: 100px'><img src='warning.png' style='width: 100px'><img src='warning.png' style='width: 100px'>
	    		<h2 style='color: black'>Exploit Detected</h2>
	    		<table style='color: black'><tr><th>File</th><th>time</th><th>UID</th><th>IP</th></tr>
	    			  <tr><td>${file}</td><td>${time}</td><td>${uid}</td><td>${ip}</td></tr>
	    			  </table>`,
	    buttons: {
	        action: {
	            title: 'Ok',
	            fn: close
	        }
	    }
	});
}