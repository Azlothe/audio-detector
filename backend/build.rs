fn main() {
    tonic_build::configure()
        .build_server(false)
        // .out_dir("src/generated")  // specify the generated code's location
        .compile_protos(
            &["proto/inference.proto"],
            &["proto"], // specify the root location to search proto dependencies
        ).unwrap();
}