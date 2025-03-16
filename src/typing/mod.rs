mod body;
mod cookie;
mod enums;
mod headers;
mod ipaddr;
mod json;
mod multipart;
mod proxy;
mod status;
mod verify;

pub use self::{
    body::FromPyBody,
    cookie::{FromPyCookieList, FromPyCookieMap, IntoPyCookieList, IntoPyCookieMap},
    enums::{Impersonate, ImpersonateOS, LookupIpStrategy, Method, TlsVersion, Version},
    headers::{
        HeaderMap, HeaderMapFromPyDict, HeaderMapItemsIter, HeaderMapKeysIter,
        HeadersOrderFromPyList,
    },
    ipaddr::{IpAddr, SocketAddr},
    json::Json,
    multipart::{Multipart, Part},
    proxy::Proxy,
    status::StatusCode,
    verify::Verify,
};
use pyo3::{prelude::*, pybacked::PyBackedStr};
use serde::ser::{Serialize, SerializeSeq, Serializer};

pub struct QueryOrForm(Vec<(PyBackedStr, PyBackedStr)>);

impl Serialize for QueryOrForm {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: Serializer,
    {
        let mut seq = serializer.serialize_seq(Some(self.0.len()))?;
        for (key, value) in &self.0 {
            seq.serialize_element::<(&str, &str)>(&(key.as_ref(), value.as_ref()))?;
        }
        seq.end()
    }
}

impl FromPyObject<'_> for QueryOrForm {
    fn extract_bound(ob: &Bound<'_, PyAny>) -> PyResult<Self> {
        ob.extract().map(Self)
    }
}
