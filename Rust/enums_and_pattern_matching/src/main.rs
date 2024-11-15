// learning structs and enums

enum IPAddrKind {
    V4,
    V6,
}

struct IPAddr {
    kind: IPAddrKind,
    address: String,
}


fn main() {
    let address1 = IPAddr {
        kind: IPAddrKind::V4

    }
}
