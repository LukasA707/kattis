open System

let input = Console.ReadLine()

let p : int = 13
let k : int = 13
let h : int = 13
let t : int = 13
let isGreska : bool = false

let map : Map<String,bool> = Map<string, bool> []

let check s : string = if s.Length > 3 then check(s.SubString(3)) if map.ContainsKey(s.SubString(0,3)) then isGreska = true else map.Add(s.)
