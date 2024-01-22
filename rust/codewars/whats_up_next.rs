// What's up next?
// https://www.codewars.com/kata/542ebbdb494db239f8000046/rust


// DESCRIPTION
// Given a sequence of items and a specific item in that sequence, return the item immediately following the item specified. 
// If the item occurs more than once in a sequence, return the item after the first occurence. This should work for a sequence of any type.
// When the item isn't present or nothing follows it, the function should return

fn next_item<T: PartialEq<T> + Clone>(slice: &[T], find: T) -> Option<T> {
    let mut iter = slice.iter().peekable();
    while let Some(item) = iter.next().cloned() {
        if item == find {
            return iter.next().cloned();
        }
    }
    None
  
}


// Best & Clever
fn next_item<T: PartialEq<T> + Clone>(slice: &[T], find: T) -> Option<T> {
    slice.iter().skip_while(|&x| *x != find).nth(1).cloned()
  }