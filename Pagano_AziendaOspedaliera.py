'''
    Progetto di Programmazione di Reti
            Arianna Pagano
            a.a. 2020/2021
       Traccia 2 - Web Server 
'''


#!/bin/env python
import sys, signal
import http.server
import socketserver

# New import
import cgi


# Legge il numero della porta dalla riga di comando, e mette default 8080
if sys.argv[1:]:
  port = int(sys.argv[1])
else:
  port = 8080

# Classe che mantiene le funzioni di SimpleHTTPRequestHandler
class ServerHandler(http.server.SimpleHTTPRequestHandler):        
    def do_GET(self):
        # Scrivo sul file AllRequestsGET le richieste dei client     
        with open("AllRequestsGET.txt", "a") as out:
          info = "GET request,\nPath: " + str(self.path) + "\nHeaders:\n" + str(self.headers) + "\n"
          out.write(str(info))
        http.server.SimpleHTTPRequestHandler.do_GET(self)
         
    def do_POST(self):
        try:
            # Salvo i vari dati inseriti
            form = cgi.FieldStorage(    
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST'})
            
            # Con getvalue prendo i dati inseriti dall'utente
            name = form.getvalue('name')
            email = form.getvalue('email')
            messaggio = form.getvalue('messaggio')

            # Stampo all'utente i dati che ha inviato
            output="Commento inviato\n\nMESSAGGIO:\nNOME e COGNOME: " + name + "\nE-MAIL: " + email + "\nCOMMENTO: " + messaggio +"\n"
            self.send_response(200)
        except: 
            self.send_error(404, 'Bad request submitted.')
            return;
        
        self.end_headers()
        self.wfile.write(bytes(output, 'utf-8'))
        
        # Salvo in locale i vari messaggi in AllPOST
        with open("AllPOST.txt", "a") as out:
          info = "\n\nPOST request,\nNOME e COGNOME: " + name + "\nE-MAIL: " + email + "\nCOMMENTO: "+ messaggio +"\n"
          out.write(info)
        
# ThreadingTCPServer per gestire più richieste
server = socketserver.ThreadingTCPServer(('',port), ServerHandler)


header_html = """
<html>
    <head>
        <style>
            h1 {
                text-align: center;
                margin: 0;
            }
            table {width:70%;}
            img {
                max-width:300;
                max-height:200px;
                width:auto;
            }
            td {width: 33%;}
            p {text-align:justify;}
            td {
                padding: 20px;
                text-align: center;
            }
            .topnav {
  		        overflow: hidden;
  		        background-color: #00705f; <!--colore azzurro riquadri affianco a home-->
  		    }
            .topnav a {
  		        float: left;
  		        color: #f2f2f2; <!--scritta nei riquadri es. analisi--> 
  		        text-align: center;
  		        padding: 14px 16px;
  		        text-decoration: none;
  		        font-size: 20px;
  		    }        
  		    .topnav a:hover {
  		        background-color: #51c4e0; <!--colore bianco quando passo sopra con mouse-->
  		        color: black;
  		    }        
  		    .topnav a.active {
  		        background-color:#4ca5af; <!--colore azzurro home-->
  		        color: white;
  		    }
        </style>
    </head>
    <body>
		<br><br><h1><strong>Azienda Ospedaliera</strong></h1> 
"""

# La barra di navigazione è identica per tutte le pagine dei servizi
navigation_bar = """
            <br>
			<br>
			<div class="topnav">
				<a class="active" href="ospedale.html">Home</a>
				<a href="prelievi.html">Prelievi per visite mediche</a>
				<a href="tamponi.html">Tamponi Molecolari</a>
				<a href="riabilitazione.html">Riabilitazione</a>
				<a href="consulenza.html">Consulenza con medici specializzati</a>
				<a href="farmaci.html">Farmaci</a>
				<a href="Relazione_PaganoArianna.pdf" download="Relazione_PaganoArianna.pdf" style="float: right">Download pdf</a>
			</div>
        <br>
        <table align="center">

""".format(port=port)


# La parte finale è identica per tutte la pagine dei servizi
footer_html= """
        </table>
    </body>
</html>
"""

end_page_home = """
</table>
		<h2><strong>Chi siamo</strong></h2>
		<p> La Azienda Ospedaliera e' un ospedale di ricerca e policlinico universitario per fornire cure specializzate per le condizioni di salute piu' complesse.
		<br> Viene fondato nel 2021 da Arianna Pagano.
		<br>Offre notevoli servizi, tra cui possiamo ricordare
		<ul>
			<li>Prelievi di ogni genere per visite mediche</li> 
			<li>Tamponi Molecolari Del COVID-19</li>
			<li>Riabilitazione con fisioterapisti</li>
			<li>Consulenza con medici specializzati</li>
			<li>Disponibilita' di consulare i farmici di cui disponiamo</li>
		</ul>
		E molto altro ancora.
		<img src="\images\ospedale.jpg" width="250" height="200" div align=right Hspace="20">
		</p>
"""

# La parte finale per la pagine principale dove è possibile fare una recensione
end_page_recensione = """
        <br><br>
        <form action="ospedale.html" method="post" style="text-align: Left;" ;>
		  <p style="text-align: left" ><i>Il tuo giudizio e' molto importante per noi.
		  <br>Ci aiuterai a migliorarci nel futuro e poter offrire maggiori cure.</i> </p>
		  <p style="text-align: left" ><strong>Lascia un commento</strong></p>
		  <label for="name">Cognome e Nome:</label><br>
		  <input type="text" id="name" name="name"><br>
		  <label for="email">Email:</label><br>
		  <input type="text" id="email" name="email"><br>
		  <label for="messaggio">Messaggio:</label><br><textarea name="messaggio" id="messaggio" rows="2"></textarea><br><br>
		  <input type="submit" value="Invia">
		</form>
		<br>
    </body>
</html>
""".format(port=port)


def create_page_prelievi():
    f = open('prelievi.html','w', encoding="utf-8") 
    f.close()
  
    
def create_page_tamponi():
    f = open('tamponi.html','w', encoding="utf-8")
    f.close()   
    
def create_page_riabilitazione():
    f = open('riabilitzione.html','w', encoding="utf-8") 
    f.close()
    
def create_page_consulenza():
    f = open('consulenza.html','w', encoding="utf-8")
    f.close()
    
def create_page_farmaci(): 
    f = open('farmaci.html','w', encoding="utf-8")
    f.close()
    
    
# Creazione della pagina ospedale.html (iniziale) contenente la schermata iniziale con la descrizione e i commenti
def create_page_ospedale():
    f = open('ospedale.html','w', encoding="utf-8") 
    try: 
        message = header_html + navigation_bar + "</table>" + end_page_home + end_page_recensione 
    except: 
       pass  
    f.write(message)
    f.close()

# Definiamo una funzione per permetterci di uscire dal processo tramite Ctrl-C
def signal_handler(signal, frame):
    print( 'Exiting http server (Ctrl+C pressed)')
    try:
      if( server ):
        server.server_close()
    finally:
      sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)



def main():
    
    # Assicura che da tastiera usando la combinazione di tasti Ctrl-C termini in modo pulito tutti i thread generati
    server.daemon_threads = True 
    
    # Il Server acconsente al riutilizzo del socket
    # Anche se ancora non è stato rilasciato quello precedente, andandolo a sovrascrivere
    server.allow_reuse_address = True  
    
    # Interrompe l'esecuzione se da tastiera arriva la sequenza (CTRL + C) 
    signal.signal(signal.SIGINT, signal_handler)
    
    # Creo pagina inziale
    create_page_ospedale()
    
    # Cancella i dati get ogni volta che il server viene attivato
    f = open('AllRequestsGET.txt','w', encoding="utf-8")
    f.close()
    
    # Entra nel loop infinito
    try:
      while True:
        server.serve_forever()
    except KeyboardInterrupt:
      pass
  
    server.server_close()

if __name__ == "__main__":
    main()
