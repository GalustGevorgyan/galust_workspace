package imageslideshow.androidopentutorials.com.pagerviewexample;

/**
 * Created by nanenare on 5/22/16.
 */
import android.graphics.Color;
import android.media.Image;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.GridView;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.LinearLayout.LayoutParams;
import android.widget.TextView;

import java.util.Random;

public final class TestFragment extends Fragment {
    private static final String KEY_CONTENT = "TestFragment:Content";
    private Integer m_res;


    public static TestFragment newInstance(Integer res) {
        TestFragment fragment = new TestFragment();
        fragment.m_res =res;
//        StringBuilder builder = new StringBuilder();
//        for (int i = 0; i < 20; i++) {
//            builder.append(content).append(" ");
//        }
//        builder.deleteCharAt(builder.length() - 1);
//        fragment.mContent = builder.toString();

        return fragment;
    }

    //private String mContent = "???";

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
//
//        if ((savedInstanceState != null) && savedInstanceState.containsKey(KEY_CONTENT)) {
//            mContent = savedInstanceState.getString(KEY_CONTENT);
//        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        ImageView mImageView = new ImageView(getActivity());
        mImageView.setImageResource(m_res);
        return  mImageView;
    }

//    public View getView(int position, View convertView, ViewGroup parent){
//        ImageView mImage;
//        if (convertView == null) {  // if it's not recycled, initialize some attributes
//            mImage = new ImageView(getActivity());
//            mImage.setLayoutParams(new GridView.LayoutParams(85, 85));
//            mImage.setScaleType(ImageView.ScaleType.CENTER_CROP);
//            mImage.setPadding(8, 8, 8, 8);
//        } else {
//            mImage = (ImageView) convertView;
//        }
//
//        mImage.setImageResource(m_res);
//        return mImage;
//    }

    @Override
    public void onSaveInstanceState(Bundle outState) {
        super.onSaveInstanceState(outState);
       // outState.putString(KEY_CONTENT, mContent);
    }
}