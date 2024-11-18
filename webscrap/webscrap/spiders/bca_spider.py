import scrapy
import deepl
import csv

# Kunci API untuk DeepL
auth_key = "df293dbf-b303-4418-8ba3-4155c91e4276"  # Ganti dengan kunci API Anda
translator = deepl.Translator(auth_key)

class BcaSpider(scrapy.Spider):
    name = "bca_spider"
    allowed_domains = ["bca.co.id"]
    start_urls = ["https://www.bca.co.id/id/bisnis/layanan/e-banking-bisnis/mybca-bisnis"]

    # Variabel untuk menyimpan data terjemahan
    translated_data = []

    def parse(self, response):
        # Mengambil teks dari elemen-elemen yang biasanya berisi konten
        paragraphs = response.xpath("//p//text()").getall()  # Mengambil teks dari <p>
        headers = response.xpath("//h1//text() | //h2//text() | //h3//text()").getall()  # Mengambil teks dari header
        other_text = response.xpath("//span//text() | //div//text()").getall()  # Mengambil teks dari elemen span dan div

        # Menggabungkan semua teks dan membersihkan
        all_text = paragraphs + headers + other_text
        clean_text = [text.strip() for text in all_text if text.strip()]  # Hapus teks kosong atau whitespace

        # Menyimpan teks yang akan diterjemahkan
        for original_text in clean_text:
            self.translated_data.append(original_text)

    def closed(self, reason):
        # Menerjemahkan teks menggunakan DeepL dan menyimpan hasilnya
        translated_rows = []
        for original_text in self.translated_data:
            try:
                translated_text = translator.translate_text(original_text, target_lang="ZH").text
                character_count = len(original_text)  # Menghitung jumlah karakter dalam teks asli
                translated_rows.append([original_text, translated_text, character_count])
            except Exception as e:
                self.log(f"Error translating text: {original_text}, error: {e}")
                continue

        # Menyimpan hasil terjemahan ke file CSV
        with open("translated_content.csv", mode="w", encoding="utf-8-sig", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Original Text", "Translated Text", "Character Count"])  # Header kolom
            writer.writerows(translated_rows)

        self.log("File translated_content.csv berhasil dibuat.")
