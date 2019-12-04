$.getJSON("/data").done(makeList);

function makeList(jsonData) {
    for (element of jsonData) {
        var info = '';
        for (information of element.informations) {
            info += '<div class="keyword">' + information + '</div>';
        }
        console.log(info);
        let item = `<li>${info} ${element.name}</li>`;
        $("ul").append(item);
    }
}