import time

# Importing WebScrappers
from webscrappers.emag_scrapper import scrapeEmag

# Importing Functions
from functions.writeCsv import writeCsv

emagLinks = [
    "https://www.emag.ro/casti-apple-airpods-2-white-mv7n2zm-a/pd/DQ8L5ZBBM/?ref=others_also_viewed_1_4&provider=rec-go&recid=rec_golang_43_cd01f53588102f44b88d86578bcb33e2_1568638750&scenario_ID=43",
    "https://www.emag.ro/telefon-mobil-samsung-galaxy-note-10-plus-dual-sim-256gb-12gb-ram-4g-aura-glow-sm-n975fzsdrom/pd/DGXRJ5BBM/?ref=fam#Aura-Glow",
    "https://www.emag.ro/joc-assassins-creed-odyssey-pentru-playstation-4-ubi4080111/pd/D6CY7SBBM/?X-Search-Id=4d6a4b022d42a99f6f6a&X-Product-Id=37145491&X-Search-Page=1&X-Search-Position=11&X-Section=search&X-MB=0&X-Search-Action=view",
    "https://www.emag.ro/trotineta-electrica-xiaomi-mijia-m365-viteza-25-km-h-autonomie-30-km-roti-8-5-timp-de-incarcare-5h-doua-anvelope-rezerva-negru-fbc4004gl-black/pd/DKXBJJBBM/?X-Search-Id=8a167c2a439882c79fcf&X-Product-Id=4651040&X-Search-Page=1&X-Search-Position=0&X-Section=search&X-MB=0&X-Search-Action=view"
]

for emagLink  in emagLinks:
    emagScrape = scrapeEmag(emagLink)
    writeCsv(emagScrape)
    time.sleep(5)