open System

let line = Console.ReadLine().Split(' ');

let number1 = line[0] |> int
let number2 = line[1] |> int

printf $"{number1 + number2}"