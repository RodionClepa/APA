use rand::prelude::*;
mod quicksort;
mod mergesort;
mod heapsort;
mod shellsort;
use std::time::Instant;
fn main() {
    let mut rng = rand::thread_rng();
    let mut number_of_elements: usize = 100;
    let mut arr_quick: Vec<f64> = Vec::new();
    let mut arr_merge: Vec<f64> = Vec::new();
    let mut arr_heap: Vec<f64> = Vec::new();
    let mut arr_shell: Vec<f64> = Vec::new();
    while number_of_elements <= 10000 {
        let mut arr: Vec<f64> = vec![0.0; number_of_elements];
        for elem in arr.iter_mut() {
            *elem = rng.gen_range(-100000.0..100000.0);
        }
        let n: usize = arr.len();
        let start_time = Instant::now();


        let mut arr_copy: Vec<f64> = arr.clone();
        quicksort::quick_sort(&mut arr_copy, 0, n - 1);
        let duration = start_time.elapsed();
        arr_quick.push(duration.as_secs_f64());

        let mut arr_copy: Vec<f64> = arr.clone();
        mergesort::merge_sort(&mut arr_copy, 0, n - 1);
        let duration = start_time.elapsed();
        arr_merge.push(duration.as_secs_f64());

        let mut arr_copy: Vec<f64> = arr.clone();
        heapsort::heap_sort(&mut arr_copy, n);
        let duration = start_time.elapsed();
        arr_heap.push(duration.as_secs_f64());

        let mut arr_copy: Vec<f64> = arr.clone();
        shellsort::shell_sort(&mut arr_copy, n);
        let duration = start_time.elapsed();
        arr_shell.push(duration.as_secs_f64());

        number_of_elements += 100;
    }
    println!("Quick: {:?}", arr_quick.iter().map(|&x| format!("{:.7}", x)).collect::<Vec<_>>());
    println!("Merge: {:?}", arr_merge.iter().map(|&x| format!("{:.7}", x)).collect::<Vec<_>>());
    println!("Heap: {:?}", arr_heap.iter().map(|&x| format!("{:.7}", x)).collect::<Vec<_>>());
    println!("Shell: {:?}", arr_shell.iter().map(|&x| format!("{:.7}", x)).collect::<Vec<_>>());

    number_of_elements = 100;
    let mut i:usize = 0;
    println!("Quick");
    while number_of_elements<=1000{
        println!("{} - {:.7}", number_of_elements, arr_quick[i]);
        i+=1;
        number_of_elements+=100;
    }
    number_of_elements = 100;
    i = 0;
    println!("Merge");
    while number_of_elements<=1000{
        println!("{} - {:.7}", number_of_elements, arr_merge[i]);
        i+=1;
        number_of_elements+=100;
    }
    number_of_elements = 100;
    i = 0;
    println!("Heap");
    while number_of_elements<=1000{
        println!("{} - {:.7}", number_of_elements, arr_heap[i]);
        i+=1;
        number_of_elements+=100;
    }
    number_of_elements = 100;
    i = 0;
    println!("Shell");
    while number_of_elements<=1000{
        println!("{} - {:.7}", number_of_elements, arr_shell[i]);
        i+=1;
        number_of_elements+=100;
    }
}
