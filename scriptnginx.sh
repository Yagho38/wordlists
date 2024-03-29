diff --git a/src/http/v2/ngx_http_v2.c b/src/http/v2/ngx_http_v2.c
index 19e5f3a0..cef8b5b5 100644
--- a/src/http/v2/ngx_http_v2.c
+++ b/src/http/v2/ngx_http_v2.c
@@ -623,6 +623,7 @@ ngx_http_v2_handle_connection(ngx_http_v2_connection_t *h2c)
 
     h2c->pool = NULL;
     h2c->free_frames = NULL;
+    h2c->frames = 0;
     h2c->free_fake_connections = NULL;
 
if (NGX_HTTP_SSL)
@@ -2589,7 +2590,7 @@ ngx_http_v2_get_frame(ngx_http_v2_connection_t *h2c, size_t length,
 
         frame->blocked = 0;
 
-    } else {
+    } else if (h2c->frames < 10000) {
         pool = h2c->pool ? h2c->pool : h2c->connection->pool;
 
         frame = ngx_pcalloc(pool, sizeof(ngx_http_v2_out_frame_t));
@@ -2613,6 +2614,15 @@ ngx_http_v2_get_frame(ngx_http_v2_connection_t *h2c, size_t length,
         frame->last = frame->first;
 
         frame->handler = ngx_http_v2_frame_handler;
+
+        h2c->frames++;
+
+    } else {
+        ngx_log_error(NGX_LOG_INFO, h2c->connection->log, 0,
+                      "http2 flood detected");
+
+        h2c->connection->error = 1;
+        return NULL;
     }
 
 #if (NGX_DEBUG)
@@ -4135,13 +4145,20 @@ ngx_http_v2_idle_handler(ngx_event_t *rev)
 
 #endif
 
+    h2scf = ngx_http_get_module_srv_conf(h2c->http_connection->conf_ctx,
+                                         ngx_http_v2_module);
+
+    if (h2c->idle++ > 10 * 1000) {
+        ngx_log_error(NGX_LOG_INFO, h2c->connection->log, 0,
+                      "http2 flood detected");
+        ngx_http_v2_finalize_connection(h2c, NGX_HTTP_V2_NO_ERROR);
+        return;
+    }
+
     c->destroyed = 0;
     c->idle = 0;
     ngx_reusable_connection(c, 0);
 
-    h2scf = ngx_http_get_module_srv_conf(h2c->http_connection->conf_ctx,
-                                         ngx_http_v2_module);
-
     h2c->pool = ngx_create_pool(h2scf->pool_size, h2c->connection->log);
     if (h2c->pool == NULL) {
         ngx_http_v2_finalize_connection(h2c, NGX_HTTP_V2_INTERNAL_ERROR);
diff --git a/src/http/v2/ngx_http_v2.h b/src/http/v2/ngx_http_v2.h
index 9e738aa5..524e5aff 100644
--- a/src/http/v2/ngx_http_v2.h
+++ b/src/http/v2/ngx_http_v2.h
@@ -115,6 +115,8 @@ struct ngx_http_v2_connection_s {
     ngx_http_connection_t           *http_connection;
 
     ngx_uint_t                       processing;
+    ngx_uint_t                       frames;
+    ngx_uint_t                       idle;
 
     size_t                           send_window;
     size_t                           recv_window;
-- 
