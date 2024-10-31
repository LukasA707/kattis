open System

let input = Console.ReadLine()

let p : int = 13
let k : int = 13
let h : int = 13
let t : int = 13
let isGreska : bool = false

let map : Map<String,bool> = Map<string, bool> []

let check s : string = if s.Length > 3 then check(s.SubString(3)) if map.ContainsKey(s.SubString(0,3)) then isGreska = true else map.Add(s.)


// let funcName string =
// if string.Count > 3
// do funcName string.subString(4,string.Count)
// 
// if (map.contians(string))
//      isGreska = true
//  else 
//      map.add(string)
//      if (string.charAt(0) == 'P)
//          P--
//      ...
//
// return 
// 
// funcName(PO1HO2KO3)
//
// if (isGreska) do printf "Greska" else do printf $"{p} {k} {h} {t}"


// PO1H02K03

// funcName(PO1HO2KO3)
    // funcName(H02K03)
        //funcName(K03)