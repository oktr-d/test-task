var map = L.map('mapid').setView([47.24071, 39.71071], 17);

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

L.Control.measureControl().addTo(map);
L.control.mousePosition().addTo(map);


var churchIcon = L.icon({iconUrl: 'icons/church.png'});
var stadiumIcon = L.icon({iconUrl: 'icons/stadium.png'});
var landscapeIcon = L.icon({iconUrl: 'icons/landscape.png'});

L.marker([47.24071, 39.71071]).addTo(map)
    .bindPopup('Парк ДГТУ')
    .openPopup();
	
L.marker([47.23929, 39.71111], {icon: churchIcon}).addTo(map)
    .bindPopup('Храм святой Татианы')
	
L.marker([47.23879, 39.71020], {icon: stadiumIcon}).addTo(map)
    .bindPopup('Минифутбольное поле ДГТУ')
	
L.marker([47.24049, 39.71191], {icon: stadiumIcon}).addTo(map)
    .bindPopup('Фитнес-клуб CityFitness')
	
L.marker([47.23945, 39.70916], {icon: landscapeIcon}).addTo(map)
    .bindPopup('Спортплощадка')