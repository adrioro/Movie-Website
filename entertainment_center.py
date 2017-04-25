import fresh_tomatoes
import media

redux = media.Movie ("Redux Riding Hood", "the familiar story of Red Riding Hood from the point of view of the big, bad wolf", "https://upload.wikimedia.org/wikipedia/en/9/9e/Redux_Riding_Hood_poster.jpg", "https://www.youtube.com/watch?v=dPDVdFS5p1g")


once_upon_a_forest = media.Movie ("Once Upon a Forest", "A story in a forest known as Dapplewood, where Furlings live alongside their teacher","https://upload.wikimedia.org/wikipedia/en/1/17/OUAF_poster.jpg", "https://www.youtube.com/watch?v=hLKuBn7_Clw")


third_pig = media.Movie ("The Third Pig", "The story of a Big Bad Wolf that eats two foolish pigs and frames the third.","https://upload.wikimedia.org/wikipedia/en/c/c2/Tales_from_the_crypt_title_shot.png", "https://www.youtube.com/watch?v=t3oQLscLDb8")


mermaid = media.Movie ("The Little Mermaid II: Return to the Sea.", "The story of a little mermaid called Melody.", "https://upload.wikimedia.org/wikipedia/en/3/33/The_Little_Mermaid_2_Poster.jpg", "https://www.youtube.com/watch?v=hfETZwvhx8I")


elvis = media.Movie ("Li'l Elvis Jones and the Truckstoppers", "The story of a group of children and their adventures in outback Australia.", "http://rcdn-4.fishpond.com.au/0002/476/084/375381/6.jpeg", "https://www.youtube.com/watch?v=4tgcg52cVLM")


timon_pumbaa = media.Movie ("Timon & Pumbaa (TV series)", "An American animated television series created by Walt Disney Television Animation", "https://upload.wikimedia.org/wikipedia/en/c/c1/TimonPumbaa.jpg", "http://www.dailymotion.com/video/x3g3tus")


movies = (redux,once_upon_a_forest,third_pig,mermaid,elvis, timon_pumbaa)
fresh_tomatoes.open_movies_page(movies)