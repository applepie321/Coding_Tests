// Safen User Input Part I - htmlspecialchars
// https://www.codewars.com/kata/56bcaedfcf6b7f2125001118


// a hacker visits your website and 
// attempts to compromise it through the use of XSS (Cross Site Scripting). 
// by injecting script tags into the website 
// through form fields which may contain malicious code
// (e.g. a redirection to a malicious website that steals personal information).

// Mission
// implement a function that converts the following potentially harmful characters:

// < --> &lt;
// > --> &gt;
// " --> &quot;
// & --> &amp;



fn html_special_chars(html: &str) -> String {
    html.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("\"", "&quot;")
}



// Clever

fn html_special_chars(html: &str) -> String {
    html.chars().fold(String::new(), |mut s, x| {
       match x {
      '<' => s.push_str("&lt;"),
      '>' => s.push_str("&gt;"),
      '"' => s.push_str("&quot;"),
      '&' => s.push_str("&amp;"),
      _ => s.push(x), 
      };
      s
    })
}