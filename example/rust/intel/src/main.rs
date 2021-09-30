mod basic_usage;
mod hypercall;

fn main() {
    unsafe {
        basic_usage::run_example();
        hypercall::run_example();
    }
}
