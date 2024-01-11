
<center><b>Opis programu - Polski:</b></center><br/>
Ten program implementuje algorytm genetyczny w celu znalezienia maksimum funkcji kwadratowej o postaci: f(x) = ax^2 + bx + c. <br/>
Algorytm genetyczny jest metaheurystyką inspirowaną procesem ewolucji biologicznej, wykorzystującą operacje genetyczne, takie jak krzyżowanie i mutacja, do ewolucji populacji osobników w kierunku optymalnych rozwiązań.

<b>Parametry Funkcji Kwadratowej</b><br/>
  a = 1<br/>
  b = -250<br/>
  c = 10000<br/>
<b>Struktura Programu</b><br/>
Program składa się z głównej funkcji main, której zadaniem jest zastosowanie algorytmu genetycznego dla rozwiązania funkcji kwadratowej. Poniżej przedstawiono główne elementy programu:<br/>

1. Generowanie Populacji Początkowej:<br/>
  Populacja początkowa składa się z losowych liczb binarnych reprezentujących potencjalne rozwiązania.
2. Krzyżowanie i Mutacja:<br/>
  Zastosowanie operacji krzyżowania między dwoma losowo wybranymi osobnikami z populacji.<br/>
  Możliwość mutacji dla każdego osobnika z określonym prawdopodobieństwem.
3. Selekcja Ruletkowa:<br/>
  Wybór osobników do reprodukcji na podstawie ich przystosowania, z użyciem mechanizmu ruletki.
4. Iteracyjna Ewolucja Populacji:<br/>
  Proces powtarza się przez określoną liczbę generacji, umożliwiając populacji dostosowanie się do optymalnych rozwiązań.
5. Zapis Wyników:<br/>
  Najlepsze wyniki z każdego uruchomienia algorytmu są zapisywane do pliku "wyniki.txt".
6. Wyniki i Statystyki:<br/>
  Znalezienie najlepszego rozwiązania spośród wszystkich prób i jego prezentacja na zakończenie działania programu.
<b>>Parametry Uruchomienia<b/><br/>
  ile_wyn = 40    # Liczba powtórzeń algorytmu genetycznego<br/>
  lb_pop = 10     # Liczba populacji<br/>
  ile_os = 12     # Liczba osobników w populacji<br/>
  pr_krzyz = 0.7  # Prawdopodobieństwo krzyżowania<br/>
  pr_mut = 0.2    # Prawdopodobieństwo mutacji<br/>

Program kończy działanie, prezentując najlepsze znalezione rozwiązanie x oraz odpowiadające mu f(x) dla funkcji kwadratowej. <br/>
Algorytm genetyczny jest efektywnym narzędziem do rozwiązywania problemów optymalizacyjnych i może być dostosowany do różnych funkcji przystosowania.
<br/>
<hr>
<br/>
<center><b>Program Description - English:</b></center> <br/>
This program implements a genetic algorithm to find the maximum of a quadratic function of the form: f(x) = ax^2 + bx + c. <br/>
The genetic algorithm is a metaheuristic inspired by the biological evolution process, utilizing genetic operations such as crossover and mutation to evolve a population of individuals towards optimal solutions.

<b>Quadratic Function Parameters</b><br/>
  a = 1<br/>
  b = -250<br/>
  c = 10000<br/>
<b>Program Structure</b><br/>
The program consists of the main function (main), which applies the genetic algorithm to solve the quadratic function. Below are the main elements of the program:

1. Generating Initial Population:<br/>
  The initial population is composed of random binary numbers representing potential solutions.
2. Crossover and Mutation:<br/>
  Applying crossover operations between two randomly chosen individuals from the population.<br/>
  Allowing mutation for each individual with a specified probability.
3. Roulette Wheel Selection:<br/>
  Selecting individuals for reproduction based on their fitness using the roulette wheel mechanism.
4. Iterative Population Evolution:<br/>
  The process repeats for a specified number of generations, allowing the population to adapt to optimal solutions.
5. Results Logging:<br/>
  The best results from each algorithm run are saved to the "results.txt" file.
6. Results and Statistics:<br/>
  Finding the best solution among all attempts and presenting it at the end of the program.
<b>>Parametry Uruchomienia<b/><br/>
  ile_wyn = 40    # Number of genetic algorithm repetitions<br/>
  lb_pop = 10     # Population size<br/>
  ile_os = 12     # Number of individuals in the population<br/>
  pr_krzyz = 0.7  # Crossover probability<br/>
  pr_mut = 0.2    # Mutation probability<br/>


The program concludes by presenting the best-found solution x and its corresponding f(x) for the quadratic function.  <br/>
The genetic algorithm is an effective tool for solving optimization problems and can be adapted to various fitness functions.




