DELETE FROM ad_category_shop WHERE id > 2;
DELETE FROM ad_category_lang WHERE id > 2;
DELETE FROM ad_category WHERE id > 2;


ALTER TABLE ad_category AUTO_INCREMENT=10;
ALTER TABLE ad_category_shop AUTO_INCREMENT=10;
ALTER TABLE ad_category_lang AUTO_INCREMENT=10;

DELETE FROM ad_product;
DELETE FROM ad_product_shop;
DELETE FROM ad_attribute_shop;
DELETE FROM ad_attribute_lang;
DELETE FROM ad_image_shop;
DELETE FROM ad_image_lang;
DELETE FROM ad_image;
DELETE FROM ad_stock_available;
DELETE FROM ad_product_lang;
DELETE FROM ad_feature_value;
DELETE FROM ad_feature_value_lang;
DELETE FROM ad_feature_shop;
DELETE FROM ad_feature;
DELETE FROM ad_feature_lang;