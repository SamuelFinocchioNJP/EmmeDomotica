# EmmeDomotica
Gestisce dispositivi arduino o raspberry connessi ad un server rest con un interfaccia web

# Dispositivo
	mac_address
	descrizione (Led, Porta, Lampadina…)
	status (ON/OFF)
	value (Stato complesso del dispositivo, rgb, gradi motore)

>Server offre API che dicono stato e valore ai dispositivi.
>Client (dispositivo) legge cosa fare dalle api interrogandolo in base al mac address.
