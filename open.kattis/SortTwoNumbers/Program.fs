open System

let input = Console.ReadLine().Split(' ')

let number1 = input[0] |> int
let number2 = input[1] |> int

if number1 < number2 then 
    printf $"{number1} {number2}" 
else 
    printf $"{number2} {number1}"
