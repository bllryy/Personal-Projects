#include <cryptopp/base64.h>
#include <cryptopp/filters.h>
#include <cryptopp/modes.h>
#include <fstream>
#include <iostream>
#include <string>

using namespace CryptoPP;

// Function to decrypt data using AES
std::string decrypt_data(const std::string& encrypted_data, const std::string& key)
{
    std::string decrypted_data;

    try
    {
        CBC_Mode<AES>::Decryption decryption(reinterpret_cast<const byte*>(key.data()), key.size(), { 0 });
        StringSource s(encrypted_data, true,
            new Base64Decoder(
                new StreamTransformationFilter(
                    decryption,
                    new StringSink(decrypted_data)
                )
            )
        );
    }
    catch (const Exception& e)
    {
        std::cerr << "Error during decryption: " << e.what() << std::endl;
    }

    return decrypted_data;
}

int main()
{
    // Replace 'your_key_here' with the correct key provided by the challenge
    std::string key = "your_key_here";

    // Read encrypted content from the file
    std::ifstream encrypted_file("encrypted_ctf_challenge.reg");
    std::string encrypted_content((std::istreambuf_iterator<char>(encrypted_file)), std::istreambuf_iterator<char>());

    // Decrypt the content
    std::string decrypted_content = decrypt_data(encrypted_content, key);

    // Write the decrypted content to a new file
    std::ofstream decrypted_file("decrypted_ctf_challenge.reg");
    decrypted_file << decrypted_content;

    std::cout << "Decryption completed. Check 'decrypted_ctf_challenge.reg' for the result." << std::endl;

    return 0;
}
