$.getJSON("/data").done(makeList);

function makeList(jsonData) {
    for (element of jsonData) {
        var info = "hello";
        for (information of element.informations) {
            info.concat(information);
        }
        let item = '<li>HM...</li>';
        $("ul").append(item);
    }
}