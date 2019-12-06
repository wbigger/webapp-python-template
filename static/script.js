$.getJSON("/data").done(makeList);

function makeList(jsonData) {
    for (element of jsonData) {
        let item = `<li><div class="accessmodifier">${element.access_modifier}</div> <div class="keyword">${element.keyword}</div> <div class="datatype">${element.data_type}</div> <div class="identificator">${element.identifier}</div></li>`
        $("ul").append(item);
    }
}