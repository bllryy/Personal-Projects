// enum: versitle tool used to represent a type that can take on one of several possible variants

fn main() {
    enum IpAddrKind {
        V4,
        V6
    }
let _four = IpAddrKind::V4;
let _six = IpAddrKind::V6;

fn route(ip_kind: IpAddrKind){}

route(IpAddrKind::V4);
route(IpAddrKind::V6);

enum IpAddrKind {
    V4(String),
    V6(String),
}

// using structs
enum IpAddrKind {
    V4,
    V6
}
struct IpAddr{
    kind: IpAddrKind,
    address: String
}

let home = IpAddr{
    kind: IpAddrKind::V4,
    address: String::from("127.0.0.1")
};
let loop black = IpAddr{
    kind: IpAddrKind::V6,
    address: String::from("::1")
}
}






}