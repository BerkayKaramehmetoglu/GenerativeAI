from translate import translate_text
from generative_ai import generate_image

def main():
    turkce_prompt = input("Türkçe prompt girin: ")
    
    ingilizce_prompt = translate_text(turkce_prompt)
    print("İngilizce Çeviri:", ingilizce_prompt)
    
    image_data = generate_image(ingilizce_prompt)
    
    if image_data:
        with open("output.png", "wb") as f:
            f.write(image_data)
        print("Görsel 'output.png' olarak kaydedildi.")

if __name__ == "__main__":
    main()
