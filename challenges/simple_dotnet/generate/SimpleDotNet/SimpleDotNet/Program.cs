// flag{51bbd5deca0f3ca0}

byte[] partOne = System.Text.Encoding.UTF8.GetBytes("Not that easy sorry :(");
byte[] partTwo = Convert.FromHexString("fb21bf9910fcf5a605234a91b536940724128c73ea4a");
byte[] partThree = Convert.FromBase64String("0yKq3h+hpbBHIh6GqXWGWDBTljLgHw==");
byte[] result = new byte[partOne.Length];

for (int i = 0; i < partOne.Length; i++)
{
    result[i] = (byte)(partOne[i] ^ partTwo[i] ^ partThree[i]);
}

Console.Write("Enter the password: ");
byte[] password = System.Text.Encoding.UTF8.GetBytes(Console.ReadLine() ?? "");

if (password.SequenceEqual(result))
{
    Console.WriteLine("Correct!");
} else
{
    Console.WriteLine("Wrong :(");
}
