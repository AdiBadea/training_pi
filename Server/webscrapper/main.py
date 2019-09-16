# Importing WebScrappers
from webscrappers.emag_scrapper import scrapeEmag

# Importing Functions
from functions.writeCsv import writeCsv

emagScrape = scrapeEmag("https://www.emag.ro/telefon-mobil-samsung-galaxy-note-10-plus-dual-sim-256gb-12gb-ram-4g-aura-glow-sm-n975fzsdrom/pd/DGXRJ5BBM/?ref=fam#Aura-Glow")

writeCsv(emagScrape)