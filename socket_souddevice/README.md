Bu kod şunu yapar;

soundfile ile serverdaki dosya sisteminde belirtilen .wav dosyasını okur;

sonrasında bunu byte formatına çevirip client'a gönderir 

client ise bu ses dosyasının bytelarını buffer a yani "int" veri tipinde 1D matrix e çevirir


en sonunda ise client sd.play(buffer) şeklinde bu alınan dosyayı çalar
