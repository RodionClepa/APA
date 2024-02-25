fn heapify(arr: &mut [f64], n: usize, i: usize){
    let mut largest: usize = i;
    let l: usize = 2*i+1;
    let r: usize = 2*i+2;

    if l<n && arr[l]>arr[largest] {
        largest = l;
    }

    if r<n && arr[r]>arr[largest] {
        largest = r;
    }

    if largest!=i{
        arr.swap(i, largest);
        heapify(arr, n, largest);
    }
}

pub fn heap_sort(arr: &mut [f64], n: usize){
    for i in (0..(n/2)).rev(){
        heapify(arr, n, i);
    }

    for i in (0..(n)).rev(){
        arr.swap(0, i);
        heapify(arr, i, 0);
    }
}