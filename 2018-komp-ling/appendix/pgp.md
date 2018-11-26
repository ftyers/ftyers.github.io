<!--
vim: tw=70
SPDX-License-Identifier: (CC-BY-SA-4.0 OR GFDL-1.3-or-later)
Copyright 2018 Nick Howell
-->

# Intro to OpenPGP

### <a name="Abstract">Abstract</a>
[#Abstract]: #Abstract

We will introduce the OpenPGP (Pretty Good Privacy) specification for
cryptographically secure communications, with an emphasis on informed
use of the `gnupg` suite of command-line utilities.

<div style="column-width:30em">

## <a name="Introduction">Introduction</a>
[#Introduction]: #Introduction

Computers essentially operate based on the results of communications:
the software you run, the people you know, the amount of money in your
bank account, how to *use* the money in your bank account, is all in
essence digital communications. The authenticity and security of all
of this is dependent on software cryptosystems, and in particular, on
the notion of **asymmetric cryptography**.

### Symmetric cryptography

You might know cryptography in the sense of **symmetric ciphers**:
there is a secret `SEC`. To encrypt a message `M`, called the
*cleartext*, you apply a mathematical operation `enc(SEC, M)`. The
result is the *ciphertext* `X`.

Anyone who knows the same secret `SEC` can apply a mathematical
operation `dec(SEC, X)` to recreate the message, that is,
```
dec(SEC, X) = dec(SEC, enc(SEC, M)) = M
```

**Exercise**: implement the Caesar cipher in python, which advances
each letter of 'M' by 'SEC = n': `enc(1, "a") = "b"`, etc.

### Asymmetric cryptography

Asymmetric cryptography works differently: there is a pair of related
keys (numbers), for now call them `A` and `B`. Just like with
symmetric cryptography, there is a mathematical operation `RSA(key, x)`.
The keys `A` and `B` have a special relationship: if a message is
encrypted with `A`, it is decrypted by `B`, and vice-versa:
```
RSA(A, RSA(B, M)) = M
RSA(B, RSA(A, M)) = M
```

Without `B`, `RSA(A, x)` cannot be decrypted, *even with `A`*.

The first system for constructing such `A`, `B`, and `RSA` is called the
[Rivest-Shamir-Adelman algorithm], after the three authors. Now there
are many such systems, not all of which can properly be called RSA.

[Rivest-Shamir-Adleman algorithm]: https://en.wikipedia.org/wiki/RSA_(cryptosystem)

### Applications to trust

Using this system, we can develop a trust system: call `A` the
"public" key; it is made available to all. The other key, `B`, is
kept secret by the owner, never revealed to anyone.

Anyone who wishes to send a message `M` to the key owner can compute
`RSA(A, M)`; only the matching secret key will be able to decrypt.


```
      enc  >--------->--------->  dec
         / RSA(A, -)   RSA(B, -) \
 A  You                            Me  A,B

```

Similarly, if the owner wishes to publish a message which has their
approval indisputably, they may compute a hash `H = H(M)` of the
message, and encrypt it with their secret key `B` to get the
*digital signature* `S = RSA(B, H)`; they send this alongside
their message.

Anyone who doubts the authenticity of the message can hash the message
to get `H(M)` and compute `RSA(A, S) = RSA(A, RSA(B, H)) = H`; if they
match, then the owner *must* have approved the message: the key `A`
can only decrypt messages encrypted by `B`, so the sender must have
`B`.

```
 A  You                            Me    A,B
         \ RSA(A, -)   RSA(B, -) /
   verify  <---------<---------<  sign

```

**Exercise** Who can verify the signature? Who can decrypt the
message? Why?

### PGP

Pretty Good Privacy is a specification for the use of asymmetric
cryptography in the ways described above.

In PGP every user has a **PGP id**, which consists of several
components:
1. List of user ids
   A list of identities for the user; these are typically of the form
   `Full Name <handle@domain.com>`, though you can have urls,
   pictures, or any other (small) identifying data.
2. Master keypair
   The keypair which binds subkeypairs, and performs Certify
   operations.
3. Subkeypairs
   Keypairs for encryption and authentication
4. Certifications
   A list of certifications (frequently called "key signatures").

A PGP identity
```
          PGP id ...FFFF0000
 |----------------------------------|
 |          master keypair [CS__]   |
 |----------------------------------|
 |             user ids             |
 | Nick Howell <nlhowell@gmail.com> | -- certifications    :)
 | Nick Howell <nlhowell@yandex.ru> | -- no certifications :(
 |----------------------------------|
 |    authenticate keypair [___A]   |
 |----------------------------------|
 |         encrypt keypair [__E_]   |
 |----------------------------------|
 |         certifications           |
 | Nick Howell <nlhowell@gmail.com> |
 | by ....EEEE1111                  |
 |                                  |
 | Nick Howell <nlhowell@gmail.com> |
 | by ....DDDD2222                  |
 |----------------------------------|

```

PGP identities are referred to by the SHA1 hash of the master public
key, called the **fingerprint**; this is a sequence of 40 hexadecimal
(0-9A-F) digits, usually displayed in 10 blocks of 4 digits:
```
   0123 4567 89AB CDEF 0123 4567 89AB CDEF FFFF 0000
```
If you want to know whether two PGP identities are the same, you
compare the **fingerprints**. A nickname for the PGP identity is the
**handle**, the last two blocks: `FFFF0000`.

As hinted above, each keypair has some **capabilities**; these are one
or more of:
1. Certify (master only)
   used to certify (private) or verify the certification (public) of
   the owner of another PGP id
2. Sign
   used to sign (private) or verify the signature (public) of messages
3. Encrypt
   used to decrypt (private) or encrypt (public) messages to this PGP
   id
4. Authenticate
   used to login to websites or other computers

### GnuPG

[GNU Privacy Guard] is a libre software implementation of the PGP
specification.

The main way of interacting with GnuPG is with the command-line tool
`gpg`. It comes by default on Linux and BSD distributions; see their
[homepage][GNU Privacy Guard] for installation on Mac or Windows.

Please check that you have a modern version of `gpg`:
```
$ gpg --version

gpg (GnuPG) 2.2.8
libgcrypt 1.8.3
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Home: /home/nlhowell/.gnupg
Supported algorithms:
Pubkey: RSA, ELG, DSA, ECDH, ECDSA, EDDSA
Cipher: IDEA, 3DES, CAST5, BLOWFISH, AES, AES192, AES256, TWOFISH,
        CAMELLIA128, CAMELLIA192, CAMELLIA256
Hash: SHA1, RIPEMD160, SHA256, SHA384, SHA512, SHA224
Compression: Uncompressed, ZIP, ZLIB, BZIP2
```

Versions of `gpg` older than `2.1.0` have serious design limitations,
and are not supported. If your `gpg` version is below `2.0.0` you may
have a `gpg2` command instead.

[GNU Privacy Guard]: https://www.gnupg.org

#### Generating a PGP identity
To generate a new PGP identity, run
```
$ gpg --gen-key
gpg (GnuPG) 2.2.8; Copyright (C) 2018 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

gpg: keybox '/tmp/test/pubring.kbx' created
Note: Use "gpg --full-generate-key" for a full featured key generation dialog.

GnuPG needs to construct a user ID to identify your key.

Real name: Nick Howell
Email address: nlhowell@gmail.com
You selected this USER-ID:
    "Nick Howell <nlhowell@gmail.com>"

Change (N)ame, (E)mail, or (O)kay/(Q)uit? O
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.

<PASSPHRASE DIALOG>

We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
gpg: /tmp/test/trustdb.gpg: trustdb created
gpg: key 31496C2CC0FD482F marked as ultimately trusted
gpg: directory '/tmp/test/openpgp-revocs.d' created
gpg: revocation certificate stored as '/tmp/test/openpgp-revocs.d/1C27E72BE87CF18EF76DF12131496C2CC0FD482F.rev'
public and secret key created and signed.

pub   rsa2048 2018-11-14 [SC] [expires: 2020-11-13]
      1C27E72BE87CF18EF76DF12131496C2CC0FD482F
uid                      Nick Howell <nlhowell@gmail.com>
sub   rsa2048 2018-11-14 [E] [expires: 2020-11-13]


```

For me, this command generated pgp id
```
      1C27 E72B E87C F18E F76D F121 3149 6C2C C0FD 482F
```
or `c0fd482f` for short.

#### Publishing PGP identities
We can publish this key to a network of keyservers (to aid
distribution of certifications):
```
$ gpg --send-keys c0fd482f # use your own handle
```

You can also export them in plaintext:
```
$ gpg --armor --export c0fd482f # use your own handle
-----BEGIN PGP PUBLIC KEY BLOCK-----

mQENBFvr2AsBCADQ1OxX5bQf5ebpI4a6fXxiL7PggyYk8sc49uCYYOgndleauMkv
Uqjn/w5SWxk04yzaIHwPdu+d31cxD//Cf/njpfEJ0DGsTrnWpArl6OpB37QG4ju4
dD4bRkEYrdYNWsyRju2HK+865ZblpOR05LPDTUnvTeE6gOd3xxFJKTQEVJpa6Zao
fAFXSuvpt59uuP2jCZX/7mwD+jornVC0hM0SI9pe+fYPBNuz4lc/+xo/0J022L1A
4ZsdBSq7C1p8EQAgWAWhTjc5dTYlvA/CqfEYD1lTr1cPlxGd+jYOqTsKiAT3fxVv
ACScMCUhyduALBnvGr3JeSrJwEnitSs079CZABEBAAG0IE5pY2sgSG93ZWxsIDxu
bGhvd2VsbEBnbWFpbC5jb20+iQFUBBMBCAA+FiEEHCfnK+h88Y73bfEhMUlsLMD9
SC8FAlvr2AsCGwMFCQPCZwAFCwkIBwIGFQoJCAsCBBYCAwECHgECF4AACgkQMUls
LMD9SC8XBwf8CtD5khIAIUA8EVXSZI/TJJUTTwYDg5t79hQZumnAvo20O8MPCIuv
EeBaFSalpvYIGR7sSKtyfyK286N1EjH6qnVb5I4vnFugR5ASrVoTG5c603uFPcf7
XOGEgs/Zbc4X9A1o2vqQeOt40Qp5rWP5zb9cUHIlslk68PMfv4EWOQPKdHoxysqb
6SWwTGkQbbkHGzoaTLXSC4hUSDlTJMC1L+J5+W++wdUj6rcEKIyYAMjUjFMoAaBq
CMZckI7VIMtanbky+EP7M3wWu51iLcdl9911cKCMLAIsoyphRgOjD8JEKY2I2Z2K
TSBlUAdFw4YmkVyq0Uw05TmWXhB5d3rjbrkBDQRb69gLAQgAxy/8KUALAEaXrLk4
X1iNX+9nOC2Bf2SyVP7t/GLO4HhYcDabO6o3qzYTtP0RmTqOok9UY4q0Bb1qBmvI
tUfcU8ijoS1egux23o2QQjaNudzd7L8psYZ7MZn08I48badBP9w5OWcA9KUPnQI7
GTTo8Hc8mkiHf4qa2HmEMXCWJdoQpjsR4+fEv5g+3Mcn7jTPydanx3my4FqKCg0c
u3B1CA7TP2rU+RCBffwvPwZQim3TmXA7VopDcPioiycsM+dKaKmgOsV+Zd/hplmK
Q/TYMhp3WQ36dvNhgZ4NgXEzgZgnmaKme2+XneiUFbRXRAxlTzBIa1Kcm8o1f0xD
Dl7A1QARAQABiQE8BBgBCAAmFiEEHCfnK+h88Y73bfEhMUlsLMD9SC8FAlvr2AsC
GwwFCQPCZwAACgkQMUlsLMD9SC930gf/cIJaOUS/rDlBDohMXWcPW/WrG3bLnDKi
5VUkbMBR6uz7c3SXERp/xd5tBHYzTfLWn3r4TVEmlmo5tyWhkG/K+MWJMVm5BO1P
GAxSYYL0z8RxvwrZs6SJHs3TIzQicjJDuMXQglJu/aaUPQt4j85iH062Oye5zO5L
vydT5+FNerdQQpJ3lPPAjAKDXSNSUUPqp8By1bM4yOmk/F16VMhMKNQc5ijcuuaw
dlO4iIkV+NThFdIiIZ5A0EYnKgftLXSFC9u/BHAMfOIuDDM89FJN43ZzCIMtM5R1
aTxeSQdi0a0QDnccajR1oX+TgvafSd80u7dAwnFetkMNCLcP6kWmVA==
=S+dY
-----END PGP PUBLIC KEY BLOCK-----
```

#### Finding (untrusted!) PGP identities
You can find other PGP identities on keyservers using `gpg
--search-keys <search-terms>` where valid search terms are
fingerprints, handles, or parts of the uid attached to the identity.
You can download my identity with
```
$ gpg --search-keys B86F7896F8768A1A173AA4EDD5A47E58DAFAAF95
```

You can also read them directly:
```
$ gpg --import # paste a public key block, e.g. mine:
-----BEGIN PGP PUBLIC KEY BLOCK-----

mDMEW73OzBYJKwYBBAHaRw8BAQdA4DvMXScQ4YghxzAHbPz9kMIoTFg4WNRBCNdy
2uA/+Em0IE5pY2sgSG93ZWxsIDxubGhvd2VsbEBnbWFpbC5jb20+iJAEExYIADgW
IQS4b3iW+HaKGhc6pO3VpH5Y2vqvlQUCW73OzAIbAwULCQgHAgYVCgkICwIEFgID
AQIeAQIXgAAKCRDVpH5Y2vqvlQlvAQCK92HibpdMnQAnzwWQpD3N7bxvAjOAv8yf
6eys2/4T+AEAvdXBU15fiSjLuoH5ZpSTqUTEeUSs+Kevuy92Pa69JgCIuQQQEwoA
HRYhBKWfJjCTy0krRHntrm6FXe5I6KnRBQJb1/3qAAoJEG6FXe5I6KnRdlECCQEL
YgXYnLbdOtmfNnCBcXBESR8rW2P8OAk+rfmxbI6VDKM+ZHSnKJ9KoPSm0YYyJTv5
4/n1zqENnVoBVXNFqHw2kAIJATwk7+e5Wte45cwXfapwUxvxUWO9lDIvBno+RSRe
zJZRYpteGOvnC1LAnPmDmkh882Aua0K6bGB5xv5rtW5cqo65uQENBFu9zswBCAC8
UH2iRAUQ1hRALhEKLsLXB/3O/QSECWBMCUd4/dN0dINrrMuTm6GH0Vyc5c4VgDD9
sGjvUoIf1ecN8433hYxkEtC3goN9AgD6ctkYsYojK4jRLrdhCOgGEE9raXDLkihz
+7MQDoQc75XXLpnAoILGoiV8/Z66GgeDi8eUDy3zzW3Xr+L+KjA73oq+AUMMmeZr
zksRFiXlhVfQA3el9J9dHKGOUG1ATTMTM9GVHErFtmajheodZgqELkyCd0WiSEGw
UhS5y6+cjgCdkMCvHAcXaZWR/gIkTtZXJXVymcxxiE+01vnBCWvt2OM1zDwI8NCa
Hw2KgWQkuz340SSz428fABEBAAGIeAQYFggAIBYhBLhveJb4dooaFzqk7dWkflja
+q+VBQJbvc7MAhsgAAoJENWkflja+q+VwsIA/A6nbSwjRcMxcr9lmIJixMzryhQE
2ShdECZoNiRGhdnQAP9pWk5X562Qlp9XPrcTwGxKFFc+1JYHQ3fwDY4pWvQGBLg4
BFu9zswSCisGAQQBl1UBBQEBB0D9k4JAo0ofntSQyfeJJxGGMkA3uqPzndxbOje5
/N0magMBCAeIeAQYFggAIBYhBLhveJb4dooaFzqk7dWkflja+q+VBQJbvc7MAhsM
AAoJENWkflja+q+VAZQA/3Q4hRv0c8sLk8bzl/9qbko3BxNhnEma67WaTTyEcomk
AQDS7Gbs7InpYKHMIeYtpcIkxAvfh0C6w5xHz1Nu/PfACw==
=uLQW
-----END PGP PUBLIC KEY BLOCK-----
^D
gpg: key D5A47E58DAFAAF95: 1 signature not checked due to a missing
key
gpg: key D5A47E58DAFAAF95: public key "Nick Howell
<nlhowell@gmail.com>" imported
gpg: Total number processed: 1
gpg:               imported: 1
gpg: marginals needed: 3  completes needed: 1  trust model: pgp
gpg: depth: 0  valid:   1  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 1u
gpg: next trustdb check due at 2020-11-13
```

A list of PGP identities known to `gpg` can be found with
```
$ gpg --list-keys
pub   rsa2048 2018-11-14 [SC] [expires: 2020-11-13]
      1C27E72BE87CF18EF76DF12131496C2CC0FD482F
uid           [ultimate] Nick Howell <nlhowell@gmail.com>
sub   rsa2048 2018-11-14 [E] [expires: 2020-11-13]

pub   ed25519 2018-10-10 [SC]
      B86F7896F8768A1A173AA4EDD5A47E58DAFAAF95
uid           [ unknown] Nick Howell <nlhowell@gmail.com>
sub   rsa2048 2018-10-10 [A]
sub   cv25519 2018-10-10 [E]
```

### Signing and Encrypting

#### Signing and verifying
You can create a signed message using `gpg --armor --sign`:
```
$ gpg --armor --clearsign
Hello
^D
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

Hello
-----BEGIN PGP SIGNATURE-----

iQEzBAEBCAAdFiEEHCfnK+h88Y73bfEhMUlsLMD9SC8FAlvr77cACgkQMUlsLMD9
SC8mawf9GCw8b2y0HOOhSGcZhniHJQHgXiRYNTyjSaX5Pv7IqJRaltJM6N3HVFf5
s2xn+sS+DhebiTqLziL3ypmNfWIqVubLqTagOs435HYX8ERfyygXNxA6udRFzb+q
9r0Dp9Q8l8/KPnAr1KEKQZ7Y5b4RL6j3oIuha0tePX8qp8v2h5u0PirRSG/qN5pY
t3XyuUETP3JmjPV/w1H2z5RewqMtf5W05yiZvFm2oG9wdjeBq07Nxe65AlZacbYv
lM5HkY8AmrSjukVF5KyfnwGhYhyLuKtuYcAerxofyEjdBDTNi22K+gIQeoQhR7wt
LNR5MbdYH5uhxiAitit2KnnDis1dwA==
=Di92
-----END PGP SIGNATURE-----
```

Anyone with your key can verify that message; paste the message:
```
$ gpg --verify
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

Hello
-----BEGIN PGP SIGNATURE-----

iQEzBAEBCAAdFiEEHCfnK+h88Y73bfEhMUlsLMD9SC8FAlvr77cACgkQMUlsLMD9
SC8mawf9GCw8b2y0HOOhSGcZhniHJQHgXiRYNTyjSaX5Pv7IqJRaltJM6N3HVFf5
s2xn+sS+DhebiTqLziL3ypmNfWIqVubLqTagOs435HYX8ERfyygXNxA6udRFzb+q
9r0Dp9Q8l8/KPnAr1KEKQZ7Y5b4RL6j3oIuha0tePX8qp8v2h5u0PirRSG/qN5pY
t3XyuUETP3JmjPV/w1H2z5RewqMtf5W05yiZvFm2oG9wdjeBq07Nxe65AlZacbYv
lM5HkY8AmrSjukVF5KyfnwGhYhyLuKtuYcAerxofyEjdBDTNi22K+gIQeoQhR7wt
LNR5MbdYH5uhxiAitit2KnnDis1dwA==
=Di92
-----END PGP SIGNATURE-----
gpg: Signature made Wed 14 Nov 2018 12:49:43 PM MSK
gpg:                using RSA key
1C27E72BE87CF18EF76DF12131496C2CC0FD482F
gpg: Good signature from "Nick Howell <nlhowell@gmail.com>" [ultimate]
```

#### Encrypting and decrypting

Anybody with your key can now encrypt a message to you using `gpg
--armor --recipient $HANDLE --encrypt`; $HANDLE can be a PGP identity
handle, fingerprint, or part of uid (e-mail or name).
```
$ gpg --armor --recipient c0fd482f --encrypt
Hello
-----BEGIN PGP MESSAGE-----

hQEMA2S2sG7AbkxzAQf+ObRvB7CwN02RMXZqb3nNV+Pw3zjh1Y+8LFSl0IjFly+M
xAj4Qp3Qk4u26mbn2e1FKNrlVkP2P2dynJPYC5dxWcuHAab3KwKBnooWiHeRf1Tn
UdEi4nTkQxgN10r+fK8gjlGu4LLV7aWt5oYokcBLnbr60qhCDfLtL5N5qtjulzmV
ORCWhVVZTP4ZDZMrpm9yZ3jZzzvEmLKJ5GNKLQP4uWfxBh6Hx9wMMHNdfM5ZR6CK
GtrZ8xoErWyh3Mx9iuMT+wUs+iTVdo2L8FKOM1ueXCJyKR/JAF/VWERhbvC6wvcu
HzMQ+kWBRkZs+Dg2qNlHin/lGmRqHd1tfiu6lWA9xdJBAUgFSimvfLu5UDrn6irQ
82FAYcuCjgvEHLSTiOxz1LBVw0/QrG5dknr75fNmwWRZf+cN01GUq7YT+ie+WfL6
TQs=
=Ln2j
-----END PGP MESSAGE-----
```

To decrypt, paste the PGP message into `gpg --decrypt`:
```
$ gpg --decrypt
-----BEGIN PGP MESSAGE-----

hQEMA2S2sG7AbkxzAQf+ObRvB7CwN02RMXZqb3nNV+Pw3zjh1Y+8LFSl0IjFly+M
xAj4Qp3Qk4u26mbn2e1FKNrlVkP2P2dynJPYC5dxWcuHAab3KwKBnooWiHeRf1Tn
UdEi4nTkQxgN10r+fK8gjlGu4LLV7aWt5oYokcBLnbr60qhCDfLtL5N5qtjulzmV
ORCWhVVZTP4ZDZMrpm9yZ3jZzzvEmLKJ5GNKLQP4uWfxBh6Hx9wMMHNdfM5ZR6CK
GtrZ8xoErWyh3Mx9iuMT+wUs+iTVdo2L8FKOM1ueXCJyKR/JAF/VWERhbvC6wvcu
HzMQ+kWBRkZs+Dg2qNlHin/lGmRqHd1tfiu6lWA9xdJBAUgFSimvfLu5UDrn6irQ
82FAYcuCjgvEHLSTiOxz1LBVw0/QrG5dknr75fNmwWRZf+cN01GUq7YT+ie+WfL6
TQs=
=Ln2j
-----END PGP MESSAGE-----
gpg: encrypted with 2048-bit RSA key, ID 64B6B06EC06E4C73, created 2018-11-14
      "Nick Howell <nlhowell@gmail.com>"
Hello
```

### Key validity

The major problem in asymmetric cryptosystems is called **validity**:
how to trust that you have the correct PGP identity for a given uid;
i.e., if a PGP id claims to have `Nick Howell <nlhowell@gmail.com>` as
a uid, is Nick Howell the real owner of the secret keys?

A major strategy in attacking asymmetric cryptosystems is to convince
the target to use a public keypair for which the attacker holds the secret
part. They can do this by stealing the secret keys, or they can do it
by tricking the target into using a public key with a forged identity.

#### Key security

The former problem can be solved by keeping your secret keys secure;
this is the purpose of the passphrase, which keeps your secret keys
encrypted when your computer is off. In the extreme, security means
secret keys are kept on an "energy-gapped" computer, and all
decryption and signing occurs there.

A more modest improvement in security is the use of a hardware
"cryptotoken" or "smartcard;" this is a small microcontroller which
holds your secret keys and lives on a usb stick. Secret keys are not
made accessible to the main computer, so malware and hackers will not
be able to steal your keys (though they *will* be able to mess with
the data sent to the token).

See [Gnuk on Blue Pill] for how to make your own cryptotokens from
200₽ microcontrollers.

[Gnuk on Blue Pill]: https://blog.dan.drown.org/gnuk-open-source-gpg-ssh-hardware-key-storage/


#### Key certification
The latter problem is solved by face-to-face verification.

If Alice and Bob wish to have secure communication, the solution is
for them to meet face-to-face and compare the fingerprints of their
PGP identities. So that they don't forget the results of this, **after
comparison** they **Certify** each-others identities. This uses the
master keypair to produce a signature of the uid+fingerprint of the
identity. (Typically all uids are signed, but in some circumstances
you want only to sign one of many uids.)

If Alice and Bob don't know each-other well, they may wish to see some
evidence that the uids they are signing are "real" in some sense:
common practices involve
* an e-mail exchange, "proving" control of the uid's e-mail address
* presentation of government-issued identification, "proving"
  "ownership" of the uid's Full Name.

To certify a key with `gpg`, you use the `gpg --sign-key` command.
**Verify the fingerprints face-to-face** and then type `y`.
```
$ gpg --sign-key $HANDLE # handle you want to certify
pub  ed25519/D5A47E58DAFAAF95
     created: 2018-10-10  expires: never       usage: SC
     trust: unknown       validity: unknown
sub  rsa2048/EB5F5719CCBFEE45
     created: 2018-10-10  expires: never       usage: A
sub  cv25519/8244BE89B2B04368
     created: 2018-10-10  expires: never       usage: E
[ unknown] (1). Nick Howell <nlhowell@gmail.com>


pub  ed25519/D5A47E58DAFAAF95
     created: 2018-10-10  expires: never       usage: SC
     trust: unknown       validity: unknown
 Primary key fingerprint: B86F 7896 F876 8A1A 173A  A4ED D5A4 7E58 DAFA AF95

     Nick Howell <nlhowell@gmail.com>

Are you sure that you want to sign this key with your
key "Nick Howell <nlhowell@gmail.com>" (31496C2CC0FD482F)

Really sign? (y/N)
```

Afterwards, `gpg --list-keys` will show the key with "full" validity,
instead of "unknown."

You can upload your signature to the keyservers by sending the
*target key*: `gpg --send-keys dafaaf95`.

#### Web of Trust

You can build a graph in which nodes are PGP identities and edges are
certifications. If you have some faith in the people you have
certified, you might be willing to assign validity to PGP identities
which you haven't personally certified, but which others have.

```
           (Nick) -------- (Danya)
	   /
	  /
	 /
      (Fran)

```

This happens in the real world constantly: you choose businesses,
doctors, friends, schools, books, all based on the recommendations of
others.

In PGP, a *trusted identity* is one which you trust to make valid
certifications; any identity which is certified by a trusted identity
`X` is valid for your identity. A *marginally trusted identity* is one
which you partly trust to make valid certifications; if enough
marginally trusted identities have certified an identity `X`, then you
consider `X` as valid.

Here, Fran's PGP id has assigned my PGP id *full trust*; since I have
certified Danya's PGP id, Fran's also considers Danya's to have full
validity.
```
                  cert
         (Nick) --------- (Danya)
  trust  /              .
  cert  /          .
       /      .    valid (no cert)
    (Fran) 
```
(note that technically these edges should be directed; it is possible
for such relationships to be asymmetric)

To assign trust with `gpg --edit-key $HANDLE`, use the `trust`
command. In the default configuration:
1. unknown trust is the default
2. untrusted marks an identity as explicitly not trusted
3. marginal trust 
   you consider a certification by this identity valid only if it is
   also certified by at least two other marginally trusted identities
4. full trust
   you consider any certification by this identity valid
5. ultimate trust is reserved for identities *you* control (i.e. for
   which you have access to the secret keys)

```
$ gpg --edit-key $HANDLE
gpg (GnuPG) 2.2.10; Copyright (C) 2018 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

pub  ed25519/D5A47E58DAFAAF95
     created: 2018-10-10  expires: never       usage: SC
     trust: unknown       validity: unknown
sub  rsa2048/EB5F5719CCBFEE45
     created: 2018-10-10  expires: never       usage: A
sub  cv25519/8244BE89B2B04368
     created: 2018-10-10  expires: never       usage: E
[ unknown] (1). Nick Howell <nlhowell@gmail.com>

gpg> trust
pub  ed25519/D5A47E58DAFAAF95
     created: 2018-10-10  expires: never       usage: SC
     trust: unknown       validity: unknown
sub  rsa2048/EB5F5719CCBFEE45
     created: 2018-10-10  expires: never       usage: A
sub  cv25519/8244BE89B2B04368
     created: 2018-10-10  expires: never       usage: E
[ unknown] (1). Nick Howell <nlhowell@gmail.com>

Please decide how far you trust this user to correctly verify other users' keys
(by looking at passports, checking fingerprints from different sources, etc.)

  1 = I don't know or won't say
  2 = I do NOT trust
  3 = I trust marginally
  4 = I trust fully
  5 = I trust ultimately
  m = back to the main menu

Your decision?
```

</div>

