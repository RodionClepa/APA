
fn partition(arr: &mut [f64], low: usize, high: usize) -> usize{
    let pivot: f64 = arr[high];
    let mut i: i32 = low.try_into().unwrap();
    i-=1;
    for j in low..=high{
        if arr[j]<pivot{
            i+=1;
            arr.swap(i.try_into().unwrap(), j);
        }
    }
    arr.swap((i+1).try_into().unwrap(), high);
    return (i+1).try_into().unwrap();
}

pub fn quick_sort(arr: &mut [f64], low: usize, high: usize){
    if low<high {
        let pi: usize = partition(arr, low, high);

        if pi > 0 {
            quick_sort(arr, low, pi-1);
        }
        quick_sort(arr, pi+1, high);
    }
}

