# Firefox Security Settings

## Security Add-ons
- [AdBlocker Ultimate](https://addons.mozilla.org/en-US/firefox/addon/adblocker-ultimate/)
- [ClearURLs](https://addons.mozilla.org/en-US/firefox/addon/clearurls/)
- [Decentraleyes](https://addons.mozilla.org/en-US/firefox/addon/decentraleyes/)
- [CanvasBlocker](https://addons.mozilla.org/en-US/firefox/addon/canvasblocker/)
- [Firefox Relay](https://relay.firefox.com/)
- [Privacy Badger](https://addons.mozilla.org/en-US/firefox/addon/privacy-badger17/)
- [uBlock Origin](https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/)
- [WebRTC Leak Shield](https://addons.mozilla.org/en-US/firefox/addon/webrtc-leak-shield/)
- [More](https://addons.mozilla.org/en-US/firefox/extensions/category/privacy-security/)

## Secure Internet Connection
- Use VPN
- Enable [Cloudfare](https://developers.cloudflare.com/1.1.1.1/setup/)
- Enable ECH
- Disable WebRTC

### VPN
Virtual private network (VPN) can provide several benefits, such as hiding your IP address, encrypting your internet traffic, and allowing you to access content that may be restricted in your region.


### Enable DoH (DNS-over-HTTPS) with Cloudflare
1. Open Firefox and go to `about:preferences#general`.
2. Scroll down to `Network Settings` and click on `Settings...`.
3. Select `Enable DNS over HTTPS` and select `Cloudflare` as provider.
4. Click `OK` and close the tab.

Or
1. Open Firefox and go to `about:config`.
2. Search for `network.trr`.
3. Set `network.trr.mode` to `2` or `3` (`2`: TRR first, fallback to DNS, `3`: TRR only)
4. Set `network.trr.uri` to `https://mozilla.cloudflare-dns.com/dns-query`.


### Enable ECH (Encrypted Client Hello)
1. Open Firefox and go to `about:config`.
2. Search for `network.dns`.
3. Set `network.dns.echconfig.enabled` to `true`.
5. Set `network.dns.http3_echconfig.enabled` to `true`.


### Disable WebRTC
```{admonition} WebRTC
👉 WebRTC stands for Web Real-Time Communication. It is a technology that allows audio and video communication over the internet directly between browsers, without the need for plugins or external software. While it can be useful for video conferencing and other real-time communication, it can also potentially leak your IP address, which is a privacy concern. Disabling WebRTC in your browser can help prevent IP leaks.
```

Disable WebRTC:
1. Open Firefox and go to `about:config`.
2. Search for `media.peerconnection.enabled` and set it to `false`.

[WebRTC Leak Shield](https://addons.mozilla.org/en-US/firefox/addon/webrtc-leak-shield/): This extension can switch the setting above easily.


## Test
- [Cloudflare Browser Check](https://www.cloudflare.com/ssl/encrypted-sni/#results)
- [WebRTC Test](https://ip8.com/webrtc-test)
- [DNS Leak Test](https://dnsleaktest.org/dns-leak-test)

If you pass [Cloudflare Browser Check](https://www.cloudflare.com/ssl/encrypted-sni/#results), you can see:
```{image} img/cloudflare-test.png
:width: 600px
:alt: Cloudflare Browser Check
```