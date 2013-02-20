audio_barcodes
==============

This project explores creating acoustic barcodes as discussed by Chris Harrison: http://www.chrisharrison.net/index.php/Research/AcousticBarcodes

For this project, I teamed up with a fellow I Schooler, Sean Chen and this was for our class, Advanced Device Design, Spring 2013.

An acoustic barcode is a series of notches on a smooth surface. The user can then run their finger or stylus over the notches, creating a series of clicks. The spacing between clicks can then be interpreted as 1s and 0s. The audio itself is picked up by a contact microphone. 

For this project we used a acoustic guitar pickup plugged into a small amp and then into our computer. The barcodes themselves were lasercut out of acrylic. The audio was feed through Pure Data with a Python extension. Pure Data processed the audio signal, throwing out background noise. It then institues a timer to get the delay between clicks. The python script then takes those delay times, and groups them into 1s and 0s, and interprets the barcode. For fun, it then opens up different websites based on the received code.

See Wiki for more details, images, and a demo video.



## License

The MIT License (MIT) 

Copyright (c) 2012 Elliot Nahman